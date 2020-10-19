from decimal import Decimal

from django.contrib import messages
from django.core.validators import MinValueValidator
from django.db import models

# from products.views import myMinValueValidator


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # se voglio aggiungere componenti alla pizza

    def get_price(self):
        return self.price

    # serve per vedere il nome effettivo del modello
    def __str__(self):
        return self.name


class Food(models.Model):
    image = models.ImageField(upload_to='dishes/', default='dishes/no-imaage-1771002-1505134.png')
    name = models.CharField(max_length=80)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    MinValueValidator.message = "Il prezzo del prodotto deve essere maggiore o uguale a 0!!"
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    def get_food_count(self):
        return self.objects.count()


class Drink(models.Model):
    name = models.CharField(max_length=50)
