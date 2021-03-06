from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _

from products.models import Food, Drink


class CustomUser(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, is_active=False, is_staff=None, is_admin=None):
        if not email:
            raise ValueError("L'utente deve avere un'email!")

        user = self.model(
            email=self.normalize_email(email)  # normalize: tutti i caratteri come lowercase
        )

        # assegno gli attributi a user
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = is_staff
        user.is_active = is_active
        user.is_admin = is_admin
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_active=True,
            is_admin=True,
            is_staff=True,
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=60, verbose_name='Nome')
    last_name = models.CharField(max_length=60, verbose_name='Cognome')
    region = models.CharField(max_length=35, verbose_name='Regione', blank=True, null=True)
    province = models.CharField(max_length=30, verbose_name='Provincia', blank=True, null=True)
    cap = models.CharField(max_length=5, verbose_name='CAP', blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name='Città', blank=True, null=True)
    via = models.CharField(max_length=50, verbose_name='Via', blank=True, null=True)
    house_number = models.CharField(max_length=10, verbose_name='Numero civico', blank=True, null=True)
    piano = models.CharField(max_length=30, blank=True, verbose_name='Piano', null=True)
    note = models.TextField(blank=True, verbose_name='Note', null=True)
    tel_regex = RegexValidator(regex=r'^\+?1?\d{10,10}$', message=('Numero di telefono errato!'))
    tel = models.CharField(validators=[tel_regex], max_length=10, verbose_name='Telefono', blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_restaurateur = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUser()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    @property
    def is_superuser(self):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def numero_prenotazioni(self):
        prenotazioni = self.prenotazioni.all().count()
        return self.prenotazioni.all().count()

    class Meta:
        verbose_name = _('Restaurant user')
        verbose_name_plural = _('Restaurant users')


# modello per riservare un tavolo
class Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, related_name="prenotazioni")
    n_people = models.PositiveIntegerField()
    reservation_name = models.CharField(max_length=50, default=None)
    reservation_last_name = models.CharField(max_length=50, default=None)
    date = models.DateTimeField(default=None)
    discount = models.PositiveIntegerField(default=0, help_text="Inserire l'ammontare dello sconto percentuale",
                                           validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f'Tavolo riservato per {self.n_people} a nome {self.reservation_name} {self.reservation_last_name}'


class TakeAway(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='takeaways')
    food = models.ManyToManyField(Food, help_text='<em>Tenere premuto Ctrl per selezionare più prodotti</em>')
    drink = models.ManyToManyField(Drink, help_text='<em>Tenere premuto Ctrl per selezionare più prodotti</em>')
    date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=40, decimal_places=2)


class Review(models.Model):
    CHOICES = (
        (1, 'Una stella'),
        (2, 'Due stelle'),
        (3, 'Tre stelle'),
        (4, 'Quattro stelle'),
        (5, 'Cinque stelle'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='review')
    rating = models.IntegerField(choices=CHOICES, default=3)
    comment = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    description = models.CharField(max_length=100)

