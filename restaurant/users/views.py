from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth import get_user_model, logout, login
from .forms import UserCreateForm, ReservationForm
from .models import BaseUserManager, Table, User

tot_table = 100  # numero di coperti


class create_user(CreateView):
    form_class = UserCreateForm
    template_name = 'users/user_creation.html'
    success_url = reverse_lazy('home')

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['address_form'] = AddressForm(self.request.POST)
    #     else:
    #         data['address_form'] = AddressForm()
    #
    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     address = context['address_form']
    #     self.object = form.save()
    #     if address.is_valid():
    #         address.instance = self.object
    #         address.save()
    #     return super().form_valid(form)


# @login_required
# def user_profile(request):
#     context = {'person': Profile.objects.get(user=request.user)}
#     return render(request, 'users/profile.html', context)

# def create_user(request):
#     if request.method == "POST":
#         form = UserCreateForm(request.POST)
#         address_form = AddressForm(request.POST)
#         f = form.is_valid()
#         f2 = address_form.is_valid()
#         if all((form.is_valid(), address_form.is_valid())):
#             user = form.save(commit=False)
#             address = address_form.save()
#             user.address = address
#             user.save()
#     else:
#         user_form = UserCreateForm()
#         address_form = AddressForm()
#         context = {"user_form": user_form, "address_form": address_form}
#         return render(request, 'users/user_creation.html', context)


def table_reserved(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            # form.save() andava anche così e con la funzione save nel form
            if request.user.is_authenticated:
                if request.user.numero_prenotazioni % 1 == 0:
                    form.cleaned_data["discount"] = 15

            Table.objects.create(**form.cleaned_data)
            return redirect(reverse_lazy('home'))
        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, 'users/table_reservation.html', context)
    else:
        if request.user.is_authenticated:
            form = ReservationForm(
                {"reservation_name": request.user.first_name, "reservation_last_name": request.user.last_name})
        else:
            form = ReservationForm()
        context = {
            'form': form
        }
        return render(request, 'users/table_reservation.html', context)


def profile_view(request):
    user = request.user
    return render(request, 'users/profile.html', {'user':user})
