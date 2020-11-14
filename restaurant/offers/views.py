from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from products.models import Food, Drink
from products.views import is_restaurateur
from .models import Offer, OfferFood, OfferDrink


@method_decorator(is_restaurateur, name='dispatch')
class CreateOfferFood(CreateView):
    model = OfferFood
    fields = ['code', 'food', 'discount']
    template_name = 'offers/create_offer.html'
    success_url = reverse_lazy('offers:offers-list')


@method_decorator(is_restaurateur, name='dispatch')
class CreateOfferDrink(CreateView):
    model = OfferDrink
    fields = ['code', 'drink', 'discount']
    template_name = 'offers/create_offer.html'
    success_url = reverse_lazy('offers:offers-list')


"""
View che mostra la lista delle offerte per i cibi e i prodotti.
"""
@login_required
def offer_list(request):
    food = OfferFood.objects.all()
    drink = OfferDrink.objects.all()
    context = {
        'food': food,
        'drink': drink,
    }
    return render(request, 'offers/offers_list.html', context)


@method_decorator(is_restaurateur, name='dispatch')
class DeleteOfferFood(DeleteView):
    model = OfferFood
    template_name = 'offers/offer_delete.html'
    success_url = reverse_lazy('offers:offers-list')


@method_decorator(is_restaurateur, name='dispatch')
class DeleteOfferDrink(DeleteView):
    model = OfferDrink
    template_name = 'offers/offer_delete.html'
    success_url = reverse_lazy('offers:offers-list')
