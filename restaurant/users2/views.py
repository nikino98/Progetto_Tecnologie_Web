from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserCreationForm
from .models import User


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/user_creation.html'
    success_url = reverse_lazy('home')
