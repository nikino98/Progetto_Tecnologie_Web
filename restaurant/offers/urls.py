from django.urls import path, include
from .views import CreateOfferFood, CreateOfferDrink, offer_list, DeleteOfferDrink, DeleteOfferFood

app_name = 'offers'
urlpatterns = [
    path('', offer_list, name='offers-list'),
    path('create_food/', CreateOfferFood.as_view(), name='offer-create-food'),
    path('create_drink/', CreateOfferDrink.as_view(), name='offer-create-drink'),
    path('delete_food/<int:pk>', DeleteOfferDrink.as_view(), name='offer-delete-drink'),
    path('delete_drink/<int:pk>', DeleteOfferFood.as_view(), name='offer-delete-food'),

]