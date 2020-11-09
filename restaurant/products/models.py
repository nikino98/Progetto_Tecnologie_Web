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


class Product(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='dishes')
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    # MinValueValidator.message = "Il prezzo del prodotto deve essere maggiore o uguale a 0!!"   validators=[MinValueValidator(Decimal('0.01'))]
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} - {self.price}€"


class Food(Product):
    ingredients = models.ManyToManyField(Ingredient)

    def get_food_count(self):
        return self.objects.count()


class Drink(Product):
    litri = models.DecimalField(max_digits=10, decimal_places=2)
