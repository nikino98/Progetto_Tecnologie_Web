from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, HTML
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.db import models
from django.forms import fields, inlineformset_factory

from users.models import User, Table, TakeAway, Comment


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'tel',
            'password1',
            'password2',
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
            'first_name': 'Inserisci il tuo nome:',
            'email': 'Inserisci la tua mail:',
            'tel': 'Inserisci il numero di telefono:',
            'password1': 'Inserisci la tua password:',
            'password2': 'Conferma la password:'
        }


class ReservationForm(forms.Form):
    n_people = forms.DecimalField(min_value=1, label='Inserisci il numero di persone della prenotazione:')
    reservation_name = forms.CharField(label='Inserisci il nome per la prenotazione: ')
    reservation_last_name = forms.CharField(label='Inserisci il cognome per la prenotazione')
    date = forms.DateTimeField(help_text="Inserisci data e l'ora nel formato YYYY-MM-DD hh:mm")


class TakeAwayForm(forms.ModelForm):
    class Meta:
        model = TakeAway
        fields = (
            'food',
            'drink',
        )

        labels = {
            'food': 'Seleziona cibi:',
            'drink': 'Seleziona bevande:',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'description',
        )

        labels = {
            'description': 'Lascia un commento'
        }

