from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML, Field, Button
from django import forms

from products.models import Food, Drink, Ingredient


class CreateProductForm(forms.ModelForm):
    # helper = FormHelper()
    # helper.form_id = 'product-create-form'
    # helper.form_method = 'POST'
    # helper.layout = Layout(
    #     Div(
    #         HTML("<h3>Inserisci un nuovo prodotto</h3>"),
    #         Field('image', 'Inserisci immagine', title='Image'),
    #         HTML('<br>'),
    #         Field('name', css_class='bg-white', title='Name'),
    #         Field('description', css_class='bg-white', title='Description'),
    #         Field('ingredients', css_class='bg-white', title='Ingredients'),
    #         Field('price', css_class='bg-white', title='Price'),
    #
    #     ),
    #     HTML('<br>'),
    #     Button('cancel', 'Annulla', css_class='btn btn-primary'), #NON VA
    #     Submit('save', 'Salva')
    # )
    # helper.add_input(Submit('salva', 'Salva'))
    price = forms.DecimalField(min_value=0.5, label='Inserisci il prezzo del piatto:')

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


class ProductModifyForm(forms.ModelForm):
    price = forms.DecimalField(min_value=0.5)

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
            'image': '<b>Modifica Immagine del piatto',
            'name': 'Nome del piatto',
            'description': 'Descrizione del piatto',
            'ingredients': 'Ingredienti del piatto',
            'price': 'Prezzo del piatto</b>',
        }


class CreateDrink(forms.ModelForm):
    price = forms.DecimalField(min_value=0.5, label='Inserisci il prezzo della bevanda:')
    litri = forms.DecimalField(min_value=0.1, label='Inserisci i litri della bevanda:')

    class Meta:
        model = Drink
        fields = (
            'image',
            'name',
            'description',
            'litri',
            'price'
        )

        labels = {
            'image': "<b>Inserisci l'immagine della bevanda che desideri, altrimenti non inserire nulla",
            'name': 'Inserisci il nome della bevanda',
            'description': 'Inserisci una descrizione della bevanda',
            'price': 'Inserisci il prezzo</b>'
        }


class DrinkModifyForm(forms.ModelForm):
    price = forms.DecimalField(min_value=0.5, label='<b>Inserisci il nuovo prezzo della bevanda:</b>')
    litri = forms.DecimalField(min_value=0.1, label='<b>Inserisci i litri della bevanda:</b>')

    class Meta:
        model = Drink
        fields = (
            'image',
            'name',
            'description',
            'litri',
            'price'
        )

        labels = {
            'image': "<b>Modifica immagine",
            'name': 'Inserisci il nome della bevanda',
            'description': 'Inserisci una descrizione della bevanda',
            'litri': 'Inserisci i litri',
            'price': 'Inserisci il prezzo</b>'
        }


class IngredientAddForm(forms.ModelForm):
    price = forms.DecimalField(min_value=0.5, label='Inserisci il prezzo')

    class Meta:
        model = Ingredient
        fields = (
            'name',
            'price'
        )

        labels = {
            'name': "Inserisci l'ingrediente"
        }

