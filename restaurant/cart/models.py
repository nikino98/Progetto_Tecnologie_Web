# from django.db import models
#
#
# # ordine di un singolo oggetto
# from django.db.models.deletion import get_candidate_relations_to_delete
#
# from products.models import Food, Drink
#
#
# class OrderItem(models.Model):
#     products = models.ManyToManyField(Food, on_delete=models.PROTECT)
#     drinks = models.ManyToManyField(Drink, on_delete=models.PROTECT)
#     date_ordered = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.product.name
#
#
# # ordine complessivo
# class Order(models.Model):
#     items = models.ManyToManyField(OrderItem)
#     date_ordered = models.DateTimeField(auto_now=True)
#
#     def get_cart_items(self):
#         return self.items.all()
#
#     def get_cart_total(self):
#         return sum([item.product.price for item in self.items.all()])
#
