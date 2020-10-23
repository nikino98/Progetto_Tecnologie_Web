from django.shortcuts import render
from users.models import User


def homepage(request):
    return render(request, 'home.html')
