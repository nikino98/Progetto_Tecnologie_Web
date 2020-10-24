from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from users.models import User, Address


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nome'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Cognome'
        self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'
        self.fields['password1'].widget.attrs['placeholder'] = 'Scegli la tua password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Ripeti la password scelta'
        self.helper = FormHelper()
        self.helper.add_input(
            Submit('submit', 'Crea un account', css_class='btn btn-success')
        )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'tel',
            'password1',
            'password2',
        )

        # labels = {
        #     'first_name': 'Mario Rossi',
        #     'email': 'mariorossi@gmail.com',
        #     'password1': 'Digita la tua password',
        #     'password2': 'Reinserisci la password'
        # }


class AddressForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = 'profile_crispy_form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Salva'))

    class Meta:
        model = Address
        fields = (
            'region',
            'province',
            'cap',
            'city',
            'via',
            'house_number',
            'piano',
            'note'
            )




