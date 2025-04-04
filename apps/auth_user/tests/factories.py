import factory
from factory.django import DjangoModelFactory


class User(DjangoModelFactory):
    class Meta:
        model = "auth_user.User"

    email = factory.Faker("safe_email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.PostGenerationMethodCall("set_password", "password")
