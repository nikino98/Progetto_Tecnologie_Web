from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML, Field
from django import forms

from products.models import Food


class CreateProductForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = 'product-create-form'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            HTML("<h3>Inserisci un nuovo prodotto</h3>"),
            Field('name', css_class='bg-white', title='Name'),
            Field('description', css_class='bg-white', title='Description'),
            Field('ingredients', css_class='bg-white', title='Ingredients'),
            Field('price', css_class='bg-white', title='Price'),

        ),
        HTML('<br>'),
        Submit('save', 'Save')
    )
    # helper.add_input(Submit('salva', 'Salva'))

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
