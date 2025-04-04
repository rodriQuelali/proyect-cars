import random
from typing import List

import pytest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from apps.auth_user.models import User
from apps.cars.models.cars import Car
from apps.cars.tests import factories as car_factories
from testing import BaseTestCase


class CarListTests(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.url = reverse("cars:car-list")

    @classmethod
    def setUpTestData(cls):
        cls.email = "email@email.com"
        cls.password = "contrasena1234"

        cls.user = User.objects.create_user(
            email=cls.email,
            password=cls.password,
            first_name="name 1",
            last_name="lastname 1",
        )
        cls.cars = car_factories.Car.create_batch(10)

    def setUp(self) -> None:
        self.login(self.email, self.user)

    def test_list(self):
        response = self.api_client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()

        self.assertEqual(len(response_data), len(self.cars))

        for car, data in zip(self.cars, response_data):
            self.assertEqual(car.make, data.pop("make"))
            self.assertEqual(car.model, data.pop("model"))
            self.assertEqual(car.year, data.pop("year"))
            self.assertEqual(car.fuel, data.pop("fuel"))
            self.assertEqual(car.speed, data.pop("speed"))
            self.assertEqual(car.id, data.pop("id"))
            self.assertFalse(data)

    def test_list__empty(self):
        Car.objects.all().delete()

        response = self.api_client.get(self.url)
        response_data = response.json()

        self.assertEqual(response_data, [])


class CarCreateTests(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.url = reverse("cars:car-list")

    @classmethod
    def setUpTestData(cls):
        cls.email = "email@email.com"
        cls.password = "contrasena1234"

        cls.user = User.objects.create_user(
            email=cls.email,
            password=cls.password,
            first_name="name 1",
            last_name="lastname 1",
        )
        cls.cars = car_factories.Car.create_batch(5)

    def setUp(self):
        self.login(self.email, self.user)

        self.data = {
            "make": "NISSAN",
            "year": 2000,
            "model": "MODEL1",
            "speed": 120,
            "fuel": 50,
        }

    def test_create(self):
        response: Response = self.api_client.post(self.url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        car_data = response.json()

        car_created = Car.objects.get(pk=car_data.pop("id"))

        self.assertEqual(car_created.make, self.data["make"])
        self.assertEqual(car_created.model, self.data["model"])
        self.assertEqual(car_created.speed, self.data["speed"])
        self.assertEqual(car_created.year, self.data["year"])
        self.assertEqual(car_created.fuel, self.data["fuel"])

        self.assertEqual(car_data.pop("make"), self.data.pop("make"))
        self.assertEqual(car_data.pop("model"), self.data.pop("model"))
        self.assertEqual(car_data.pop("speed"), self.data.pop("speed"))
        self.assertEqual(car_data.pop("fuel"), self.data.pop("fuel"))
        self.assertEqual(car_data.pop("year"), self.data.pop("year"))
        self.assertFalse(self.data)
        self.assertFalse(car_data)

        data = {
            "make": "TOYOTA",
            "year": 2000,
            "model": "MODEL1",
            "speed": 120,
            "fuel": 50,
        }
        response = self.api_client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CarRetrieveTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cars: List[Car] = car_factories.Car.create_batch(5)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.id = cls.cars[3].pk

        cls.url = reverse("cars:car-details", kwargs={"pk": cls.id})

    @classmethod
    def setUpTestData(cls):
        cls.cars: List[Car] = car_factories.Car.create_batch(5)

    @pytest.mark.skip("Add back when tests for retrieve are completed")
    def test_retrieve(self):
        response: Response = self.api_client.patch(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data_car = response.json()

        self.assertEqual(self.id, data_car["id"])

        print("response> ", response.json())

        # TODO: complete respective vlaidations and missing tests
        # Rodrigo
        # raise


class CarDeleteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cars: List[Car] = car_factories.Car.create_batch(5)

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.api_client = APIClient()

        cls.id = cls.cars[3].pk

        cls.url = reverse("cars:car-details", kwargs={"pk": cls.id})

    def test_delete(self):
        response: Response = self.api_client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(response.content, b"")

        print("response>>>>", response.content)

        # raise


class CarUpdateTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cars: List[Car] = car_factories.Car.create_batch(5)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.api_client = APIClient()

        id = cls.cars[2].pk

        cls.url = reverse("cars:car-details", kwargs={"pk": id})

    def setUp(self):
        self.data = {"model": "model modified", "year": 1000}

    @pytest.mark.skip("Add back when tests for update are completed")
    def test_update(self):
        response = self.api_client.patch(self.url, data=self.data)

        print("response> ", response.json())

        # TODO: complete respective vlaidations and missing tests
        # Luis
        raise


class CarSummaryTests(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.required_make = cls.cars[5].make

        cls.url = reverse("cars:make-summary", kwargs={"make_name": cls.required_make})

    @classmethod
    def setUpTestData(cls):
        cls.email = "email@email.com"
        cls.password = "contrasena1234"

        cls.user = User.objects.create_user(
            email=cls.email,
            password=cls.password,
            first_name="name 1",
            last_name="lastname 1",
        )

        makes = ["toyota", "nissan", "mercedez benz", "bugatti", "subaru"]

        cls.cars: List[Car] = []

        for make in makes:
            cls.cars.extend(
                car_factories.Car.create_batch(random.randint(1, 10), make=make)
            )

    def setUp(self):
        self.login(self.email, self.user)

    def test_summary(self):
        response = self.api_client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()

        related_cars = list(filter(lambda c: c.make == self.required_make, self.cars))

        self.assertEqual(len(response_data), len(related_cars))

        for car, data_car in zip(related_cars, response_data):
            self.assertEqual(car.model, data_car["model"])

    def test_summary__empty(self):
        url = reverse("cars:make-summary", kwargs={"make_name": "unexisting_make_name"})

        response = self.api_client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        self.assertEqual(response_data, [])
