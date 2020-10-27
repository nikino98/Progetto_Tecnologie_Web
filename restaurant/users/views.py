from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth import get_user_model, logout, login
from .forms import UserCreateForm, AddressForm, ReservationForm
from .models import BaseUserManager, Address, Profile, Table, User

tot_table = 100  #numero di coperti

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/user_creation.html'
    success_url = reverse_lazy('home')


@login_required
def user_profile(request):
    context = {'person': Profile.objects.get(user=request.user)}
    return render(request, 'users/profile.html', context)


# def table_reserved(request):
#     # if tot_table > 100:   PROVO A FARLO CON AJAX
#     #     error
#

# da finire
def table_reserved(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid() or request.POST:
        form.save()
        return reverse_lazy('home')
    else:
        form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'users/table_reservation.html', context)


# class TableReserve(CreateView):
#     model = Table
#     template_name = 'users/table_reservation.html'
#     form_class = ReservationForm
#     success_url = '../../'


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
