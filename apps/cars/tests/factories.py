import factory
from factory.django import DjangoModelFactory
from faker import Faker

fake = Faker()


class Car(DjangoModelFactory):
    class Meta:
        model = "cars.Car"

    make = factory.Sequence(lambda n: f"Company {n}")
    year = factory.LazyAttribute(lambda n: int(fake.year()))
    model = factory.Sequence(lambda n: f"Model {n}")
    speed = factory.Faker("random_number")
    fuel = factory.Faker("random_number")
