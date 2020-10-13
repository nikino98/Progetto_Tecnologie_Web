from django.shortcuts import render, get_object_or_404

# Create your views here.
from users.models import User


def add_to_cart(request, **kwargs):
    #get the user
    user = get_object_or_404(User, user=request.user)
    #filter products by id
    