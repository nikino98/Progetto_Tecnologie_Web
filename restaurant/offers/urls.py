from django.urls import path, include
from .views import CreateOfferFood, CreateOfferDrink, offer_list

app_name = 'offers'
urlpatterns = [
    path('', offer_list, name='offers-list'),
    path('create_food/', CreateOfferFood.as_view(), name='offer-create-food'),
    path('create_drink/', CreateOfferDrink.as_view(), name='offer-create-drink'),

]