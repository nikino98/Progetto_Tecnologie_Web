from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from products.models import Food, Drink
from .models import Offer, OfferFood, OfferDrink


class CreateOfferFood(CreateView):
    model = OfferFood
    fields = ['code', 'food', 'discount']
    template_name = 'offers/create_offer.html'
    success_url = reverse_lazy('offers:offers-list')


class CreateOfferDrink(CreateView):
    model = OfferDrink
    fields = ['code', 'drink', 'discount']
    template_name = 'offers/create_offer.html'
    success_url = reverse_lazy('offers:offers-list')


@login_required
def offer_list(request):
    food = OfferFood.objects.all()
    drink = OfferDrink.objects.all()
    context = {
        'food': food,
        'drink': drink,
    }
    return render(request, 'offers/offers_list.html', context)
