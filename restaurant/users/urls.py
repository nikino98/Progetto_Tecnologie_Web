from django.urls import path
from django.contrib.auth import views as auth_views
from restaurant import views
from users.views import UserCreateView, logout_view

app_name = 'users'
urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='user-creation'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
]

