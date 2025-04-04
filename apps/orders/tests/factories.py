import factory
from factory.django import DjangoModelFactory
from faker import Faker

fake = Faker()


class Order(DjangoModelFactory):
    class Meta:
        model = "orders.Order"

    user = factory.SubFactory("apps.auth_user.tests.factories.User")
    car = factory.SubFactory("apps.cars.tests.factories.Car")
    amount = 1
