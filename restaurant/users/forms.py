from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django import forms



# class UserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['first_name'].widget.attrs['placeholder'] = 'Nome'
#         self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'
#         self.helper = FormHelper
#         self.helper.add_input(
#             Submit('submit', 'Crea un account', css_class='btn btn-success')
#         )
#
#     class Meta:
#         model = User
#         fields = (
#             'first_name',
#             'last_name',
#             'password1',
#             'password2',
#         )
#
#         labels = {
#             'first_name': 'Mario Rossi',
#             'email': 'mariorossi@gmail.com',
#             'password1': 'Digita la tua password',
#             'password2': 'Reinserisci la password'
#         }
#
#         def save(self):
#             user = super().save(commit=False)
#             return user


