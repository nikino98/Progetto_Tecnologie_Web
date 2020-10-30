from django.urls import path, include
from .views import CreateOfferFood, CreateOfferDrink, offer_list

app_name = 'offers'
urlpatterns = [
    path('', offer_list, name='offers-list'),
    path('create/', CreateOfferFood.as_view(), name='offer-create'),

]