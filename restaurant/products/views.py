from django.contrib.auth.decorators import permission_required, login_required
from django.core.validators import MinValueValidator
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import Food
from .forms import CreateProductForm, UpdateProductForm
from django.contrib import messages
from users.models import User


class ProductListView(ListView):
    model = Food
    template_name = 'products/food/product_list.html'


# decoratore per verificare che gli utenti abbiano i permessi di ristoratori
def is_restaurateur(function):
    def wrapper(*args, **kwargs):
        request = args[0]
        if request is not None:
            user = request.user
            try:
                if user.is_restaurateur:
                    return function(*args, **kwargs)
                else:
                    return render(request, 'users/authentication_error.html', {})
            except AttributeError:
                raise Http404   #per utenti anonimi
    return wrapper


@is_restaurateur
def create_food(request):
    form = CreateProductForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        redirect_url = reverse('products:product-list')
        messages.success(request, 'Prodotto inserito correttamente')
        return redirect(redirect_url)

    context = {
        'form': form,
    }

    return render(request, 'products/food/product_create.html', context)


# def delete_food(request, id):
#     Food.objects.get(id=id).delete()
#     messages.success(request, 'Prodotto eliminato correttamente!')
#     context = {
#         'messages': messages,
#     }
#     return render(request, 'products/food/product_list.html', context)

class DeleteProduct(DeleteView):
    model = Food
    template_name = 'products/food/product_delete.html'
    success_url = reverse_lazy('products:product-list')


# FUNZIONA
def modify_product(request, pk):
    form = UpdateProductForm(request.POST, request.FILES)
    food = get_object_or_404(Food, pk=pk)
    if request.POST and form.is_valid():
        food.name = form.cleaned_data['name']
        food.description = form.cleaned_data['description']
        food.ingredients.set(form.cleaned_data['ingredients'])
        food.image = form.cleaned_data['image']
        food.price = form.cleaned_data['price']
        food.save()
        messages.success(request, 'Piatto modificato correttamente!')
        redirect_url = reverse('products:product-list')
        return redirect(redirect_url)

    context = {
        'form': form,
        'food_name': food.name,
    }

    return render(request, 'products/food/product_update.html', context)
