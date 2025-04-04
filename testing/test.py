from django.test import TestCase
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from apps.auth_user.models import User

__all__ = [
    "BaseTestCase",
]


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.api_client: APIClient = APIClient()

        cls.__login_url = reverse("auth:token_obtain_pair")

    def login(self, user: User):
        data = {
            "email": user.email,
            "password": "password",
        }

        response: Response = self.api_client.post(self.__login_url, data=data)

        assert response.status_code != status.HTTP_401_UNAUTHORIZED, response.json()

        access_token = response.json()["access"]
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)

    def logout(self):
        self.api_client.credentials()
