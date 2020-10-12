from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class StaffUser(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, is_staff=None, is_admin=None):
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
        user.is_admin = is_admin
        user.save(using=self.db)
        return user

    def create_superuser(self, email, first_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            password=password,
            is_admin=True,
            is_staff=True
        )
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True)
    first_name = models.CharField(max_length=60)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


class ManagerProfile():
    pass


class Profile():
    pass
