from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
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

    if form.is_valid():
        form.save()
        redirect_url = reverse('home')
        messages.success(request, 'Prodotto inserito correttamente')
        return redirect(redirect_url)

    context = {
        'form': form
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

