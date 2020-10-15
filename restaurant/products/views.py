from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Food
from .forms import CreateProductForm
from django.contrib import messages


class ProductListView(ListView):
    model = Food
    template_name = 'products/food/product_list.html'


class ProductDetailView(DetailView):
    model = Food
    template_name = 'products/food/product_detail.html'


def create_food(request):
    form = CreateProductForm(request.POST or None)
    form.ingredients = form.fields['ingredients']

    if form.is_valid():
        form.save()
        messages.success(request, 'Prodotto inserito correttamente')
        redirect_url = reverse('home')
        return redirect(redirect_url)

    context = {
        'form': form
    }

    return render(request, 'products/food/product_create.html', context)
