from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, is_active=False, is_staff=None, is_admin=None):
        if not email:
            raise ValueError("L'utente deve avere un'email!")

        user = self.model(
            email=self.normalize_email(email)   # normalize: tutti i caratteri come lowercase
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

    def create_superuser(self, email, first_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            password=password,
            is_active=True,
            is_admin=True,
        )
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    tel = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUser()

    def __str__(self):
        return self.email

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = _('Restaurant user')
        verbose_name_plural = _('Restaurant users')

class ManagerProfile():
    pass


class Profile():
    pass
