from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout
from django.core.checks import messages
from django.core.exceptions import ValidationError
from django.forms import forms, ModelForm


from users2.models import User


class UserCreationForm(ModelForm):
    helper = FormHelper()
    helper.add_input(
        Submit('submit', 'Conferma', css_class='btn btn-success')
    )
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',

        ]

    def save(self):
        user = User(self.cleaned_data)
        if not self.password_check():
            raise ValueError("Sei un semo")
        user = super().save()
        return user

    def password_check(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            return False
        return True
