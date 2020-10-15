from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # se voglio aggiungere componenti alla pizza

    def get_price(self):
        return self.price

    # serve per vedere il nome effettivo del modello
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Drink(models.Model):
    name = models.CharField(max_length=50)
