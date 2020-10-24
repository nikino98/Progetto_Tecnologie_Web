from django.urls import path
from django.contrib.auth import views as auth_views
from restaurant import views
from users.views import UserCreateView, AddressList, AddressDelete, AddressCreate, AddressModify, user_profile

app_name = 'users'

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='user-creation'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', user_profile, name='profile'),
    path('address/add/', AddressCreate.as_view(), name='address-add'),
    path('address/delete/', AddressDelete.as_view(), name='address-delete'),
    path('address/modify/', AddressModify.as_view(), name='address-modify'),
    path('address/list/', AddressList.as_view(), name='address-list'),
]
