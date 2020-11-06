from django.test import TestCase
from django.urls import reverse

from products.apps import ProductsConfig
from products.models import Ingredient, Product, Food
from users.models import User


class Tests_add_product(TestCase):

    def setUp(self):
        self.user = User()
        self.user.email = 'ciccio@gmail.com'
        self.user.first_name = 'ciccio'
        self.user.last_name = 'marolo'
        self.user.region = 'Emilia Romagna'
        self.user.province = 'MO'
        self.user.cap = '41054'
        self.user.city = 'Modena'
        self.user.via = 'Della pace'
        self.user.house_number = '38'
        self.user.piano = '1'
        self.user.tel = '3332134567'
        self.user.is_restaurateur = True
        self.user.save()
        self.client.force_login(self.user)

    def test_add_product(self):
        self.ingredients = Ingredient()
        self.ingredients.name = 'tartufo'
        self.ingredients.price = 10
        self.ingredients.save()
        response = self.client.post(
            reverse('products:product-create'),
            data={'name': 'Tagliolini al tartufo', 'ingredients': [self.ingredients.pk], 'price': 18}
        )
        self.assertTrue(Food.objects.filter(name="Tagliolini al tartufo").exists())
        self.assertEqual(response.status_code, 302) # se il form è stato submittato correttamente