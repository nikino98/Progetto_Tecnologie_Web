from django.shortcuts import render
from django.views.generic import ListView
from .models import Food


class ProductListView(ListView):
    model = Food
    template_name = 'products/product_list.html'
