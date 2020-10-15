from django.urls import path, include

from products.views import ProductListView, create_food

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', create_food, name='product-create'),
]