from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from products.models import Product

#
# class Offer(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     code = models.CharField(max_length=30)
#     discount = models.PositiveIntegerField(default=10, help_text="Inserire l'ammontare dello sconto senza percentuale!",
#                                            validators=[MinValueValidator(1), MaxValueValidator(100)])
