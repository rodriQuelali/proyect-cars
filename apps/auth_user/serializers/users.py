from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.auth_user.models import User

__all__ = [
    "UserRegisterSerializer",
]


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields: tuple[str, ...] = [
            "first_name",
            "last_name",
            "password",
            "email",
        ]

    password = serializers.CharField(write_only=True)

    def validate_first_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "First name can not be shorter than 3 letters."
            )
        return value

    def validate(self, attrs):
        password = attrs.pop("password")
        hashed_password = make_password(password)
        attrs["password"] = hashed_password
        return attrs
