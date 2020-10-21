from django.urls import path

from restaurant import views
from users2.views import UserCreateView

app_name = 'users'
urlpatterns = [
    path('user_create2/', UserCreateView.as_view(), name='user-create-2'),
]