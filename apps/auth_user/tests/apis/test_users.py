from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from apps.auth_user.models import User


class UserRegisterTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.api_client = APIClient()

        cls.url = reverse("users:user-list")

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            email="email@email.com",
            password="contrasena1234",
            first_name="name 1",
            last_name="lastname 1",
        )

    def setUp(self) -> None:
        self.data = {
            "email": "email2@gmail.com",
            "password": "contrasena1234",
            "first_name": "Rodrigo",
            "last_name": "Quelali",
        }

    def test_create(self):
        # TODO: complete validation cases
        user_count = User.objects.count()

        response = self.api_client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(User.objects.count(), user_count + 1)
        # esponse_data = response.json()
        user_created = User.objects.get(email=self.data["email"])

        self.assertTrue(user_created.check_password("contrasena1234"))


class UserLoginTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.api_client = APIClient()

        cls.url = reverse("auth:token_obtain_pair")

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            email="email@email.com",
            password="contrasena1234",
            first_name="name 1",
            last_name="lastname 1",
        )

    def setUp(self) -> None:
        self.data = {
            "email": "email@email.com",
            "password": "contrasena1234",
        }

    def test_login(self):
        response = self.api_client.post(self.url, data=self.data)

        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("access", response_data)
        self.assertIn("refresh", response_data)

        # TODO: Add missing validations
