from django.urls import path

from restaurant import views
from users.views import homepage

app_name = 'users'
urlpatterns = [
    path('', homepage, name='ciao')
]

