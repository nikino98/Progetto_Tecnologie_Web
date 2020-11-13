from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from products.models import Product, Food, Drink


class Offer(models.Model):
    code = models.CharField(max_length=7, unique=True)
    discount = models.PositiveIntegerField(default=10, help_text="Inserire l'ammontare dello sconto senza percentuale!",
                                           validators=[MinValueValidator(1), MaxValueValidator(100)])

    class Meta:
        abstract = True

    def __str__(self):
        return f"Codice: {self.code} - Sconto: {self.discount}%"


class OfferFood(Offer):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__() + f"per {self.food}"


class OfferDrink(Offer):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__() + f"per {self.drink}"
