from django.shortcuts import render
from django.views.generic import CreateView

from .models import Offer


class CreateOffer(CreateView):
    model = Offer
    template_name = 'offers/create_offer.html'
    success_url = 'offers/offers_list.html'
