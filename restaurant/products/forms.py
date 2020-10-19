from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML, Field, Button
from django import forms

from products.models import Food


class CreateProductForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = 'product-create-form'
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            HTML("<h3>Inserisci un nuovo prodotto</h3>"),
            Field('image', 'Inserisci immagine', title='Image'),
            HTML('<br>'),
            Field('name', css_class='bg-white', title='Name'),
            Field('description', css_class='bg-white', title='Description'),
            Field('ingredients', css_class='bg-white', title='Ingredients'),
            Field('price', css_class='bg-white', title='Price'),

        ),
        HTML('<br>'),
        Button('cancel', 'Annulla', css_class='btn btn-primary'), #NON VA
        Submit('save', 'Salva')
    )
    # helper.add_input(Submit('salva', 'Salva'))

    class Meta:
        model = Food
        fields = (
            'image',
            'name',
            'description',
            'ingredients',
            'price'
        )

        labels = {
            'image': "Inserisci l'immagine del cibo che desideri, altrimenti non inserire nulla",
            'name': 'Inserisci il nome del cibo',
            'description': 'Inserisci una descrizione del cibo',
            'ingredients': 'Inserisci gli ingredienti',
            'price': 'Inserisci il prezzo'
        }


class UpdateProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit('submit', 'Conferma', css_class='btn btn-success')
        )

    class Meta:
        model = Food
        fields = (
            'image',
            'name',
            'description',
            'ingredients',
            'price',
        )

        labels = {
            'image': 'Immagine del piatto',
            'name': 'Nome del piatto',
            'description': 'Descrizione del piatto',
            'ingredients': 'Ingredienti del piatto',
            'price': 'Prezzo del piatto',
        }

