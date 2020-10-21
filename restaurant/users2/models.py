from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50, error_messages={'not_same': 'Le due password non corrispondono!!'})
    password2 = models.CharField(max_length=50)
