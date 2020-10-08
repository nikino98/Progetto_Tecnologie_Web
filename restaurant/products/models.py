from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2) # se voglio aggiungere componenti alla pizza

    def get_price(self):
        return self.price


class Food(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    ingredients = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Drink(models.Model):
    nome = models.CharField(max_length=50)


