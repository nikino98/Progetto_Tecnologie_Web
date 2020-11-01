from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator, MaxValueValidator
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
        user.password = password
        user.is_staff = is_staff
        user.is_active = is_active
        user.is_admin = is_admin
        user.save(using=self.db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_active=True,
            is_admin=True,
            is_staff=True,
        )
        user.save(using=self.db)
        return user


# class Address(models.Model):
#     region = models.CharField(max_length=35)
#     province = models.CharField(max_length=30)
#     cap = models.CharField(max_length=5)
#     city = models.CharField(max_length=50)
#     via = models.CharField(max_length=50)
#     house_number = models.CharField(max_length=10)
#     piano = models.CharField(max_length=30, blank=True)
#     note = models.TextField(blank=True)
#
#     def __str__(self):
#         return f'{self.cap} - {self.city} - Via/Piazza {self.via} - num. {self.house_number}'
#
#     class Meta:
#         verbose_name_plural = 'Addresses'


class User(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    region = models.CharField(max_length=35)
    province = models.CharField(max_length=30)
    cap = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    via = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)
    piano = models.CharField(max_length=30, blank=True)
    note = models.TextField(blank=True)
    tel = models.CharField(max_length=20)
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

    def has_perms(self, perm, obj=None):
        if self.is_restaurateur:
            return True
        else:
            return HttpResponseRedirect('')

    def has_module_perms(self, app_label):
        return True

    @property
    def numero_prenotazioni(self):
        return self.prenotazioni.all().count()

    class Meta:
        verbose_name = _('Restaurant user')
        verbose_name_plural = _('Restaurant users')


# modello per riservare un tavolo
class Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, related_name="prenotazioni")
    n_people = models.DecimalField(max_digits=2, decimal_places=0)
    reservation_name = models.CharField(max_length=50, default=None)
    reservation_last_name = models.CharField(max_length=50, default=None)
    date = models.DateTimeField(default=None, null=True)
    discount = models.PositiveIntegerField(default=0, help_text="Inserire l'ammontare dello sconto percentuale",
                                           validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f'Tavolo riservato per {self.n_people} a nome {self.reservation_name} {self.reservation_last_name}'


class TakeAway(models.Model):
    food = models.ManyToManyField(Food, help_text='<em>Tenere premuto Ctrl per selezionare più prodotti</em>')
    drink = models.ManyToManyField(Drink, help_text='<em>Tenere premuto Ctrl per selezionare più prodotti</em>')
    price = models.DecimalField(max_digits=40, decimal_places=2)
