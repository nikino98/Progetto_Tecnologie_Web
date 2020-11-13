from sqlite3.dbapi2 import Date

from django.test import TestCase
from django.urls import reverse

from products.models import Food, Ingredient, Drink
from users.models import User, Table, TakeAway
from django.utils import timezone


class Tests_user_profile(TestCase):

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
        self.user.save()
        self.client.force_login(self.user)

        self.tavolo = Table()
        self.tavolo.user = self.user
        self.tavolo.n_people = 4
        self.tavolo.reservation_name = self.user.first_name
        self.tavolo.reservation_last_name = self.user.last_name
        self.tavolo.date = '2020-11-26 12:15'
        self.tavolo.save()

        self.ingredients = Ingredient()
        self.ingredients.name = 'tartufo'
        self.ingredients.price = 10
        self.ingredients.save()

        self.food = Food()
        self.food.name = 'Taglionili al tartufo'
        self.food.price = 18
        self.food.save()
        self.food.ingredients.add(self.ingredients.id)  #per il manytomany
        self.food.save()

        self.drink = Drink()
        self.drink.name = 'Vino Rosso'
        self.drink.price = 25
        self.drink.litri = 0.75
        self.drink.save()

        self.takeaway = TakeAway()
        self.takeaway.user = self.user
        self.takeaway.price = 43
        self.takeaway.save()
        self.takeaway.food.add(self.food.id)
        self.takeaway.drink.add(self.drink.id)

        self.takeaway.save()

    def test_profile_view(self):
        response = self.client.get(reverse('users:user-profile'))
        self.assertEqual(response.status_code, 200) #se non ci sono errori nella richiesta HTTP
        for p in response.context['prenotazioniDopo']:
            self.assertGreater(p.date, timezone.now())
        for p in response.context['prenotazioniPrima']:
            self.assertLess(p.date, timezone.now())

        self.assertQuerysetEqual(response.context['takeaways'], [repr(self.takeaway)])
        self.assertEqual(response.context['user'], self.user)

