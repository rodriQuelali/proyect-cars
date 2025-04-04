import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from apps.auth_user.tests import factories as user_factories
from apps.cars.tests import factories as car_factories
from apps.orders.models import Order
from apps.orders.tests import factories as order_factories
from testing import BaseTestCase


class OrderCreateTests(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.url = reverse("orders:order-list")

    @classmethod
    def setUpTestData(cls):
        cls.user = user_factories.User()
        cls.car = car_factories.Car()

    def setUp(self):
        self.login(self.user)

        self.data = {
            "client": self.user.pk,
            "car": self.car.pk,
            "amount": 1,
        }

    def test_access(self):
        response: Response = self.api_client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.logout()
        response: Response = self.api_client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @pytest.mark.skip("Remove once validation tests are completed.")
    def test_create(self):
        # TODO: Luis
        order_count = Order.objects.count()

        response: Response = self.api_client.post(self.url, data=self.data)
        from pprint import pprint

        pprint(response.json())

        self.assertEqual(Order.objects.count(), order_count + 1)
        raise
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # car_data = response.json()

        # car_created = Car.objects.get(pk=car_data.pop("id"))

        # self.assertEqual(car_created.make, self.data["make"])
        # self.assertEqual(car_created.model, self.data["model"])
        # self.assertEqual(car_created.speed, self.data["speed"])
        # self.assertEqual(car_created.year, self.data["year"])
        # self.assertEqual(car_created.fuel, self.data["fuel"])

        # self.assertEqual(car_data.pop("make"), self.data.pop("make"))
        # self.assertEqual(car_data.pop("model"), self.data.pop("model"))
        # self.assertEqual(car_data.pop("speed"), self.data.pop("speed"))
        # self.assertEqual(car_data.pop("fuel"), self.data.pop("fuel"))
        # self.assertEqual(car_data.pop("year"), self.data.pop("year"))
        # self.assertFalse(self.data)
        # self.assertFalse(car_data)

        # data = {
        #     "make": "TOYOTA",
        #     "year": 2000,
        #     "model": "MODEL1",
        #     "speed": 120,
        #     "fuel": 50,
        # }
        # response = self.api_client.post(self.url, data=data)

        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
