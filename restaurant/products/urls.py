from django.urls import path, include

from products.views import ProductListView, create_food, DeleteProduct, modify_product

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', create_food, name='product-create'),
    path('delete/<int:pk>/', DeleteProduct.as_view(), name='product-delete'),
    path('update/<int:pk>/', modify_product, name='product-update'),
   # path('delete/<int:id>/', delete_food, name='product-delete'),
]
