from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, HTML
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.db import models
from django.forms import fields, inlineformset_factory

from users.models import User, Table


class UserCreateForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['first_name'].widget.attrs['placeholder'] = 'Nome'
    #     self.fields['last_name'].widget.attrs['placeholder'] = 'Cognome'
    #     self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'
    #     self.fields['address'].widget.attrs['placeholder'] = 'example@example.com'
    #     self.fields['password1'].widget.attrs['placeholder'] = 'Scegli la tua password'
    #     self.fields['password2'].widget.attrs['placeholder'] = 'Ripeti la password scelta'
    #     self.helper = FormHelper()
    #     self.helper.add_input(
    #         Submit('submit', 'Crea un account', css_class='btn btn-success')
    #     )

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


# UserAddressFormSet = inlineformset_factory(User, Address, fields=(
#             # 'first_name',
#             # 'last_name',
#             # 'email',
#             # 'tel',
#             'region',
#             'province',
#             'cap',
#             'city',
#             'via',
#             'house_number',
#             'piano',
#             'note'
#             # 'password1',
#             # 'password2',
# ))


# class AddressForm(forms.ModelForm):
#     helper = FormHelper()
#     helper.form_id = 'profile_crispy_form'
#     helper.form_method = 'POST'
#     helper.add_input(Submit('submit', 'Salva'))
#
#     class Meta:
#         model = Address
#         fields = (
#             'region',
#             'province',
#             'cap',
#             'city',
#             'via',
#             'house_number',
#             'piano',
#             'note'
#         )


# class ReservationForm(forms.ModelForm):
#     helper = FormHelper()
#     helper.form_id = 'table-reservation-crispy'
#     helper.form_method = 'POST'
#     helper.layout = Layout(
#
#     )
#     helper.add_input(Submit('submit', 'Salva'))
#
#     class Meta:
#         model = Table
#         fields = (
#             'n_people',
#             'reservation_name',
#             'reservation_last_name',
#             'date',
#         )
#
#         labels = {
#             'n_people': 'Inserisci il numero di persone per la prenotazione:',
#             'reservation_name': 'Inserisci il nome per la prenotazione:',
#             'reservation_last_name': 'Inserisci il cognome per la prenotazione',
#         }


# class IntegerRangeField(models.IntegerField):
#     def __init__(self, *args, **kwargs):
#         kwargs['min_value'] = 0
#         kwargs['label'] = 'Inserisci il numero di persone: '
#         super().__init__(*args, **kwargs)
#
#

class ReservationForm(forms.Form):
    n_people = forms.DecimalField(min_value=1, label='Inserisci il numero di persone della prenotazione:')
    reservation_name = forms.CharField(label='Inserisci il nome per la prenotazione: ')
    reservation_last_name = forms.CharField(label='Inserisci il cognome per la prenotazione')
    date = forms.DateTimeField(help_text='Inserisci data nel formato YYYY-MM-DD.')

    def save(self):
        data = self.cleaned_data
        table = Table(
            n_people=data['n_people'],
            reservation_name=data['reservation_name'],
            reservation_last_name=data['reservation_last_name'],
            date=data['date']
        )
        table.save()

    # class Meta:
    #     model = Table
    #     fields = (
    #         'n_people',
    #         'reservation_name',
    #         'reservation_last_name',
    #         'date',
    #     )

