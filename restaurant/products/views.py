from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Food


class ProductListView(ListView):
    model = Food
    template_name = 'products/food/product_list.html'


class ProductDetailView(DetailView):
    model = Food
    template_name = 'products/food/product_detail.html'
