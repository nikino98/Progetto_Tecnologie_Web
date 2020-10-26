from django.contrib import admin

# Register your models here.
from products.models import Food, Drink, Ingredient

admin.site.register(Food)
admin.site.register(Drink)
admin.site.register(Ingredient)
