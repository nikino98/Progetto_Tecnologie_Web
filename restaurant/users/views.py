from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth import get_user_model, logout, login

from products.models import Food, Drink
from .forms import UserCreateForm, ReservationForm, TakeAwayForm, CommentForm
from .models import BaseUserManager, Table, User, TakeAway, Review, Comment

tot_table = 100  # numero di coperti


class create_user(CreateView):
    form_class = UserCreateForm
    template_name = 'users/user_creation.html'
    success_url = reverse_lazy('home')


def table_reserved(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            # form.save() andava anche così e con la funzione save nel form
            if request.user.is_authenticated:
                if request.user.numero_prenotazioni % 15 == 0:   #ogni 15 prenotazioni ho uno sconto
                    form.cleaned_data["discount"] = 15

            t = Table.objects.create(**form.cleaned_data)
            t.user = request.user
            t.save()
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
    return render(request, 'users/profile.html', {'user': user})


def create_takeaway(request):
    if request.method == "POST":
        form = TakeAwayForm(request.POST)
        if form.is_valid():
            price_food = 0
            price_drink = 0
            food_list = ""
            drink_list = ""
            for f in form.cleaned_data['food']:
                price_food += f.price
                food_list += str(f.id)+"_"

            for d in form.cleaned_data['drink']:
                price_drink += d.price
                drink_list += str(d.id)+"_"



            # form.save() andava anche così e con la funzione save nel form
            #context = {"total": price_food + price_drink}
            #Table.objects.create(**form.cleaned_data)
            return redirect(reverse_lazy("users:takeaway-redirect", args=(str(price_food + price_drink), food_list,
                                                                          drink_list)))

    else:
        form = TakeAwayForm()
        context = {
            'form': form
        }
        return render(request, 'users/take_away.html', context)


def takeaway_redirect(request, total="", food_list="", drink_list=""):
    if request.method == 'POST':
        food_list_int = food_list.split("_")
        food_list_int.pop()
        for i in range(len(food_list_int)):
            food_list_int[i] = int(food_list_int[i])

        drink_list_int = drink_list.split("_")
        drink_list_int.pop()
        for i in range(len(drink_list_int)):
            drink_list_int[i] = int(drink_list_int[i])

        total = float(total)
        t = TakeAway()
        t.price = Decimal(total) + Decimal(2)
        t.save()
        t.food.add(*food_list_int)
        t.drink.add(*drink_list_int)

        return redirect(reverse_lazy('home'))
    else:
        return render(request, 'users/riepilogo_takeaway.html', {"total": total})


def review_list(request):
    return render(request, 'users/user_review.html', {'reviews': Review.objects.all().order_by('date')})


def review_create_ajax(request):
    if request.POST:
        rating = int(request.POST.get('numero_stelle'))
        review_comment = request.POST.get('review_comment')
        user_pk = request.POST.get('user')
        user = User.objects.get(pk=user_pk)
        review = Review(rating=rating, comment=review_comment, user=user)
        review.save()
        return render(request, "users/new_review.html", {"review": review})


def comment_create(request, **kwargs):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            t = Comment(**form.cleaned_data)
            t.user = request.user
            review_pk = kwargs.get("review_pk", False)
            review = Review.objects.get(pk=review_pk)
            t.review = review
            t.save()
            return redirect(reverse_lazy('home'))
        else:
            context = {
                'form': form,
                'error': True,
            }
            return render(request, 'users/comment_create.html', context)
    else:
        form = CommentForm()
        context = {
            'form': form
        }
        return render(request, 'users/comment_create.html', context)

def comment_list(request, **kwargs):

    review_pk = kwargs.get("review_pk", False)
    review = Review.objects.get(pk=review_pk)
    comments = Comment.objects.filter(review=review_pk)
    context = {"comments": comments}
    return render(request, 'users/comment_list.html', context)