from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserCreationForm
from .models import BaseUserManager


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/user_creation.html'
    success_url = reverse_lazy('home')




