from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth import get_user_model, logout, login
from .forms import UserCreateForm, AddressForm
from .models import BaseUserManager, Address, Profile


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/user_creation.html'
    success_url = reverse_lazy('home')


@login_required
def user_profile(request):
    context = {'person': Profile.objects.get(user=request.user)}
    return render(request, 'users/profile.html', context)


class AddressCreate(CreateView):
    model = Address
    template_name = 'address/address_add.html'
    form_class = AddressForm


class AddressModify(UpdateView):
    pass


class AddressDelete(DeleteView):
    pass


class AddressList(ListView):
    pass
