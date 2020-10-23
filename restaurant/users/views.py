from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, logout, login
from .forms import UserCreateForm
from .models import BaseUserManager


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/user_creation.html'
    success_url = reverse_lazy('home')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

