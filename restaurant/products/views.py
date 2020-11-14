from django.contrib.auth.decorators import permission_required, login_required
from django.core.validators import MinValueValidator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Food, Drink, Ingredient
from .forms import CreateProductForm, CreateDrink, DrinkModifyForm, ProductModifyForm, IngredientAddForm
from django.contrib import messages
from users.models import User
from django.core.files import File


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
                raise Http404  # per utenti anonimi

    return wrapper


def product_view(request):
    drink = Drink.objects.all()
    food = Food.objects.all()
    return render(request, 'products/food/product_list.html', {'drink': drink, 'food': food})


@is_restaurateur
def create_food(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect_url = reverse('products:product-list')
            return redirect(redirect_url)
        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, 'products/food/product_create.html', context)
    else:
        form = CreateProductForm()
        context = {
            'form': form
        }
        return render(request, 'products/food/product_create.html', context)


@is_restaurateur
def create_drink(request):
    if request.method == 'POST':
        form = CreateDrink(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect_url = reverse('products:product-list')
            return redirect(redirect_url)
        else:
            context = {
                'form': form,
                'error': True
            }

        context = {
            'form': form,
        }

        return render(request, 'products/drink/drink_create.html', context)
    else:
        form = CreateDrink()
        context = {
            'form': form
        }
        return render(request, 'products/drink/drink_create.html', context)


@method_decorator(is_restaurateur, name='dispatch')
class DeleteProduct(DeleteView):
    model = Food
    template_name = 'products/food/product_delete.html'
    success_url = reverse_lazy('products:product-list')


@method_decorator(is_restaurateur, name='dispatch')
class DeleteDrink(DeleteView):
    model = Drink
    template_name = 'products/drink/drink_delete.html'
    success_url = reverse_lazy('products:product-list')


"""
View che permette la modifica dei cibi. Nella post vengono assegnati gli attributi che vengono modificati
dall'utente: nel campo immagine vengono effettuati due controlli:
    - se il valore è False, cioè l'immagine viene eliminata, allora viene assegnata una stringa vuota al campo immagine
    - se il valore è None, cioè non viene eseguita alcuna modifica all'immagine, si passa oltre.
Infine viene salvato il prodotto.
"""
@method_decorator(is_restaurateur, name='dispatch')
class ProductModify(UpdateView):
    model = Food
    template_name = 'products/food/product_update.html'
    form_class = ProductModifyForm
    success_url = reverse_lazy('products:product-list')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            # form.cleaned_data['image'] = request.POST['image']
            # form.save()
            food = get_object_or_404(Food, pk=kwargs.get('pk'))
            food.name = form.cleaned_data['name']
            food.description = form.cleaned_data['description']
            food.ingredients.set(form.cleaned_data['ingredients'])
            if form.cleaned_data['image'] is False:
                food.image = ''
            elif form.cleaned_data['image'] is None:
                pass
            else:
                food.image.delete()
                food.image = form.cleaned_data['image']
            food.price = form.cleaned_data['price']
            food.save()
            return HttpResponseRedirect(reverse_lazy('products:product-list'))
        else:
            return self.form_invalid(form)


@method_decorator(is_restaurateur, name='dispatch')
class DrinkModify(UpdateView):
    model = Drink
    template_name = 'products/drink/drink_modify.html'
    form_class = DrinkModifyForm
    success_url = reverse_lazy('products:product-list')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            # form.cleaned_data['image'] = request.POST['image']
            # form.save()
            drink = get_object_or_404(Drink, pk=kwargs.get('pk'))
            drink.name = form.cleaned_data['name']
            drink.description = form.cleaned_data['description']
            drink.litri = form.cleaned_data['litri']
            if form.cleaned_data['image'] is False:
                drink.image = ''
            elif form.cleaned_data['image'] is None:
                pass
            else:
                drink.image.delete()
                drink.image = form.cleaned_data['image']
            drink.price = form.cleaned_data['price']
            drink.save()
            return HttpResponseRedirect(reverse_lazy('products:product-list'))
        else:
            return self.form_invalid(form)


@method_decorator(is_restaurateur, name='dispatch')
class IngredientAdd(CreateView):
    template_name = 'products/food/ingredients_add.html'
    model = Ingredient
    form_class = IngredientAddForm
    success_url = reverse_lazy('products:ingredient-list')


@method_decorator(is_restaurateur, name='dispatch')
class IngredientDelete(DeleteView):
    template_name = 'products/food/ingredients_delete.html'
    model = Ingredient
    success_url = reverse_lazy('products:ingredient-list')


@method_decorator(is_restaurateur, name='dispatch')
class IngredientList(ListView):
    template_name = 'products/food/ingredients_list.html'
    model = Ingredient
