from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User as AuthUser

from .models import Product, Transaction, User


class HomeViewTests(TestCase):
    def setUp(self):
        self.auth_user = AuthUser.objects.create_user(
            username="tester",
            password="testpass123",
        )

    def test_home_page_shows_available_products_and_selected_account_transactions(self):
        selected_user = User.objects.create(
            name="Alice",
            email="alice@example.com",
            credit=12.5,
            is_subscriber=True,
        )
        other_user = User.objects.create(
            name="Bob",
            email="bob@example.com",
            credit=4,
            is_subscriber=False,
        )
        discounted_product = Product.objects.create(
            name="Panini",
            price=4.0,
            available=True,
            has_subscriber_discount=True,
        )
        other_product = Product.objects.create(
            name="Jus",
            price=2.0,
            available=True,
            has_subscriber_discount=False,
        )
        hidden_product = Product.objects.create(
            name="Secret item",
            price=8.0,
            available=False,
        )
        Transaction.objects.create(user=selected_user, product=discounted_product)
        Transaction.objects.create(user=other_user, product=other_product)

        self.client.login(username="tester", password="testpass123")
        response = self.client.get(reverse("cafeteria_app:home"), {"account": selected_user.pk})

        self.assertContains(response, "Panini")
        self.assertNotContains(response, "Secret item")
        self.assertContains(response, "Transactions du compte")
        self.assertContains(response, "Alice")
        self.assertContains(response, "3,50 €")
        self.assertNotContains(response, "Jus</td>")

    def test_home_redirects_anonymous_users_to_login(self):
        response = self.client.get(reverse("cafeteria_app:home"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("cas_ng_login"), response.url)

    def test_product_list_displays_subscriber_discount_price(self):
        Product.objects.create(
            name="Panini",
            price=4.0,
            available=True,
            has_subscriber_discount=True,
        )

        self.client.login(username="tester", password="testpass123")
        response = self.client.get(reverse("cafeteria_app:product_list"))

        self.assertContains(response, "4,00 €")
        self.assertContains(response, "3,50 €")

    def test_product_list_displays_message_when_no_subscriber_discount(self):
        Product.objects.create(
            name="Jus",
            price=2.0,
            available=True,
            has_subscriber_discount=False,
        )

        self.client.login(username="tester", password="testpass123")
        response = self.client.get(reverse("cafeteria_app:product_list"))

        self.assertContains(response, "2,00 €")
        self.assertContains(response, "Pas de réduction")
