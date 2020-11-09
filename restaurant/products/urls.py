from django.urls import path, include
from products.views import create_food, DeleteProduct, create_drink, product_view, DeleteDrink, \
    DrinkModify, ProductModify, modify_product, IngredientAdd, IngredientList, IngredientDelete

app_name = 'products'
urlpatterns = [
    # path('', ProductListView.as_view(), name='product-list'),
    path('', product_view, name='product-list'),
    path('create/', create_food, name='product-create'),
    path('delete/<int:pk>/', DeleteProduct.as_view(), name='product-delete'),
    path('update/<int:pk>/', ProductModify.as_view(), name='product-update'),
    path('create_drink/', create_drink, name='drink-create'),
    path('delete_drink/<int:pk>/', DeleteDrink.as_view(), name='drink-delete'),
    path('update_drink/<int:pk>/', DrinkModify.as_view(), name='drink-update'),
    path('add_ingredients/', IngredientAdd.as_view(), name='ingredient-add'),
    path('list_ingredients/', IngredientList.as_view(), name='ingredient-list'),
    path('list_ingredients/delete/<int:pk>', IngredientDelete.as_view(), name='ingredient-delete'),
   # path('delete/<int:id>/', delete_food, name='product-delete'),
]
