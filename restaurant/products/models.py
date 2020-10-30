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
    name = models.CharField(max_length=80)
    description = models.TextField()
    MinValueValidator.message = "Il prezzo del prodotto deve essere maggiore o uguale a 0!!"
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} - {self.price}€"


class Food(Product):
    image = models.ImageField(default='dishes/no-image-1771002-1505134.png', null=True, blank=True, upload_to='dishes')
    ingredients = models.ManyToManyField(Ingredient)

    def get_food_count(self):
        return self.objects.count()


class Drink(Product):
    litri = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
