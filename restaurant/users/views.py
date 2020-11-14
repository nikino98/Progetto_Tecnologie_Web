
from decimal import Decimal
from sqlite3.dbapi2 import Date

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.datetime_safe import datetime
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth import get_user_model, logout, login

from products.models import Food, Drink
from products.views import is_restaurateur
from .forms import UserCreateForm, ReservationForm, TakeAwayForm, CommentForm
from .models import BaseUserManager, Table, User, TakeAway, Review, Comment


def is_client(function):
    def wrapper(*args, **kwargs):
        request = args[0]
        if request is not None:
            user = request.user
            try:
                if not user.is_restaurateur and not user.is_admin and not user.is_staff:
                    return function(*args, **kwargs)
                else:
                    return render(request, 'users/authentication_error.html', {})
            except AttributeError:
                raise Http404   #per utenti anonimi
    return wrapper


class create_user(CreateView):
    form_class = UserCreateForm
    template_name = 'users/user_creation.html'
    success_url = reverse_lazy('home')


"""
View che permette di riservare un tavolo per un cliente. Quando un utente registrato arriva a 15 prenotazioni,
gli viene applicato uno sconto del 15%. Negli orari di chiusura, se un utente vuole prenotare, gli viene 
segnalato un errore. Se l'utente è autenticato, i campi del nominativo sono precompilati.
"""
def table_reserved(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            # form.save() andava anche così e con la funzione save nel form
            if request.user.is_authenticated:
                if request.user.numero_prenotazioni % 15 == 0 and request.user.numero_prenotazioni != 0 and not request.user.restaurateur:   #ogni 15 prenotazioni ho uno sconto
                    form.cleaned_data["discount"] = 15

            if form.cleaned_data['date'].hour > 11 and form.cleaned_data['date'].hour < 15 or \
                    form.cleaned_data['date'].hour > 18 and form.cleaned_data['date'].hour < 23:
                t = Table.objects.create(**form.cleaned_data)
                if not request.user.is_anonymous:
                    t.user = request.user
                t.save()
                return redirect(reverse_lazy('home'))
            else:
                context = {
                    'form': form,
                    'closed': True
                }
                return render(request, 'users/table_reservation.html', context)
        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, 'users/table_reservation.html', context)
    else:
        if request.user.is_authenticated and not request.user.is_restaurateur:  # il ristoratore può prenotare per i clienti che chiamano
            form = ReservationForm(
                {"reservation_name": request.user.first_name, "reservation_last_name": request.user.last_name})
        else:
            form = ReservationForm()
        context = {
            'form': form
        }
        return render(request, 'users/table_reservation.html', context)

"""
View per la visualizzazione del profilo. Le prenotazioni vengono divise in prenotazioni passate e future rispetto
la data in cui ci troviamo.
"""
@is_client
def profile_view(request):
    user = request.user
    prenotazioniDopo = user.prenotazioni.filter(date__gt=Date.today())
    prenotazioniPrima = user.prenotazioni.filter(date__lt=Date.today())
    takeaways = user.takeaways.all()
    return render(request, 'users/profile.html', {'user': user, 'prenotazioniDopo': prenotazioniDopo, 'prenotazioniPrima': prenotazioniPrima, 'takeaways': takeaways})


@method_decorator(is_client, name='dispatch')
class UpdateUser(UpdateView):
    model = User
    template_name = 'users/user_modify.html'
    success_url = reverse_lazy('users:user-profile')

    fields = (
        'first_name',
        'last_name',
        'email',
        'tel',
        'region',
        'province',
        'cap',
        'city',
        'via',
        'house_number',
        'piano',
        'note'
    )

    labels = {
        'first_name': 'Inserisci il nuovo nome:',
        'last_name': 'Inserisci il nuovo cognome',
        'email': 'Inserisci la nuova mail:',
        'tel': 'Inserisci il nuovo numero di telefono:',
        'region': 'Inserisci la nuova regione:',
        'province': 'Inserisci la nuova provincia:',
        'cap': 'Inserisci il nuovo CAP:',
        'city': 'Inserisci la nuova città:',
        'via': 'Inserisci la nuova via:',
        'house_number': 'Inserisci il nuovo numero di casa',
        'piano': 'Inserisci il nuovo piano',
        'note': 'Inserisci le note:'
    }

    def get_object(self, queryset=None):
        obj = User.objects.get(id=self.kwargs['id'])
        return obj


"""
View che permette la creazione di un ordine d'asporto. Vengono create due liste di prodotti che conterrano gli id 
dei food e dei drink e vengono separate da "_". Vengono poi passate ad un'altra view senza essere salvati.
"""
@is_client  # per prenotare d'asporto, l'utente deve essere autenticato, quindi non ha senso farlo fare al ristoratore. Si è deciso di non fare gestire questo aspetto al ristoratore
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

            return redirect(reverse_lazy("users:takeaway-redirect", args=(str(price_food + price_drink), food_list,
                                                                          drink_list)))

    else:
        form = TakeAwayForm()
        context = {
            'form': form
        }
        return render(request, 'users/take_away.html', context)


"""
View che estende quella precendente e che assegna effettivamente i drink e i food nel caso ci fosse una conferma
da parte dell'utente, facendo un'analisi delle due liste.
"""
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
        t.user = request.user
        t.price = Decimal(total) + Decimal(2)
        t.save()
        t.food.add(*food_list_int)
        t.drink.add(*drink_list_int)

        return redirect(reverse_lazy('home'))
    else:
        return render(request, 'users/riepilogo_takeaway.html', {"total": total})


def review_list(request):
    return render(request, 'users/user_review.html', {'reviews': Review.objects.all().order_by('date')})


@is_client
def review_create_ajax(request):
    if request.POST:
        rating = int(request.POST.get('numero_stelle'))
        review_comment = request.POST.get('review_comment')
        user_pk = request.POST.get('user')
        user = User.objects.get(pk=user_pk)
        review = Review(rating=rating, comment=review_comment, user=user)
        review.save()
        return render(request, "users/new_review.html", {"review": review})


"""
View che permette la creazione di un commento all'interno della review e che viene associata all'utente corrispondente.
"""
@login_required()
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
            return redirect(reverse_lazy('users:review-list'))
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


@login_required()
def delete_prenotazione(request):
    prenotazione_pk = request.POST.get('prenotazione_pk')
    prenotazione = Table.objects.get(pk=prenotazione_pk)
    prenotazione.delete()
    return HttpResponse(prenotazione_pk)


@is_restaurateur
def restaurateur_view(request):
    tables = Table.objects.filter(date__gt=Date.today())
    today = datetime.today()
    takeaways = TakeAway.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)
    context = {
        'tables': tables,
        'takeaways': takeaways
    }
    return render(request, 'users/restaurarìteur_view.html', context)


