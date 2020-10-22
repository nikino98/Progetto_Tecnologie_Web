from django.urls import path

from restaurant import views
from users.views import UserCreateView

app_name = 'users'
urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='user-creation'),
]

