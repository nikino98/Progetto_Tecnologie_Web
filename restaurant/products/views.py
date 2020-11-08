from django.contrib.auth.decorators import permission_required, login_required
from django.core.validators import MinValueValidator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import Food, Drink
from .forms import CreateProductForm, CreateDrink, DrinkModifyForm, ProductModifyForm
from django.contrib import messages
from users.models import User


# class ProductListView(ListView):
#     model = Food
#     template_name = 'products/food/product_list.html'


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

        # context = {
        #     'form': form,
        # }
        #
        # return render(request, 'products/food/product_create.html', context)
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


@is_restaurateur
def modify_product(request, pk):
    if request.method == 'POST':
        form = ProductModifyForm(Food, request.FILES)
        food = get_object_or_404(Food, pk=pk)
        if request.POST and form.is_valid():
            food.name = form.cleaned_data['name']
            food.description = form.cleaned_data['description']
            food.ingredients.set(form.cleaned_data['ingredients'])
            food.image = form.cleaned_data['image']
            food.price = form.cleaned_data['price']
            food.save()
            #messages.success(request, 'Piatto modificato correttamente!')
            redirect_url = reverse('products:product-list')
            return redirect(redirect_url)

        context = {
            'form': form,
            'food_name': food.name,
        }
        return render(request, 'products/food/product_update.html', context)
    else:
        form = ProductModifyForm({
                'image': Food.objects.get(pk=11).image.name,
                'name': Food.objects.get(pk=11).name,
                'description': Food.objects.get(pk=11).description,
                #'ingredients': Food.objects.filter(pk=11).ingredients,
             })
        context = {
            'form': form,
        }

        return render(request, 'products/food/product_update.html', context)


@method_decorator(is_restaurateur, name='dispatch')
class ProductModify(UpdateView):
    model = Food
    template_name = 'products/food/product_update.html'
    form_class = ProductModifyForm
    success_url = reverse_lazy('products:product-list')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        t = form.is_valid()
        if form.is_valid():
            # form.cleaned_data['image'] = request.POST['image']
            # form.save()
            food = get_object_or_404(Food, pk=kwargs.get('pk'))
            food.name = request.POST['name']
            food.description = request.POST['description']
            food.ingredients.set(form.cleaned_data['ingredients'])
            food.image.delete()
            food.image = 'dishes/' + request.POST['image']
            food.price = request.POST['price']
            food.save(update_fields=['image'])
            return HttpResponseRedirect(reverse_lazy('products:product-list'))
        else:
            return self.form_invalid(form)


@method_decorator(is_restaurateur, name='dispatch')
class DrinkModify(UpdateView):
    model = Drink
    template_name = 'products/drink/drink_modify.html'
    form_class = DrinkModifyForm
    success_url = reverse_lazy('products:product-list')

    # def post(self, request, *args, **kwargs):
    #     drink_pk = kwargs.get('pk', False)
    #     drink = Drink.objects.get(pk=drink_pk)
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     t = form.is_valid()
    #     if form.is_valid():
    #         #form.cleaned_data['image'] = request.POST['image']
    #         drink.image = request.POST['image']
    #         drink.save()
    #         return reverse_lazy('products:product-list')
    #     else:
    #         return self.form_invalid(form)