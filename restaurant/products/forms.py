from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from products.models import Food


class CreateProductForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = 'product-create-form'
    helper.form_method = 'POST'
    helper.add_input(Submit('salva', 'Salva'))

    class Meta:
        model = Food
        fields = (
            'name',
            'description',
            'ingredients',
            'price'
        )

        labels = {
            'name': 'Inserisci il nome del cibo',
            'description': 'Inserisci una descrizione del cibo',
            'ingredients': 'Inserisci la lista degli ingredienti',
            'price': 'Inserisci il prezzo'
        }
