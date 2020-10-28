from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from products.models import Product


class Offer(models.Model):
    product = models.ForeignKey(Product)
    code = models.CharField(max_length=30)
    discount = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])