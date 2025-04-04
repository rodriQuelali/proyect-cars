from rest_framework import serializers

from apps.auth_user.models import User
from apps.cars.models import Car
from apps.orders.models import Order

__all__ = ["OrderSerializer"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields: tuple[str, ...] = (
            "id",
            "client",
            "car",
            "amount",
            "placed_on",
        )
        read_only_fields: tuple[str, ...] = ("placed_on", "id")

    client = serializers.CharField(source="user.full_name")
    car = serializers.CharField(source="car.__str__")
    placed_on = serializers.DateTimeField(source="created_at", read_only=True)

    def validate(self, attrs):
        user_id = attrs.pop("user")["full_name"]
        car_id = attrs.pop("car")["__str__"]

        car_obj = Car.objects.filter(pk=car_id).first()
        user_obj = User.objects.filter(pk=user_id).first()

        if not car_obj:
            raise serializers.ValidationError(
                f"Car ID provided does not exist [{car_id}]"
            )
        if not user_obj:
            raise serializers.ValidationError(
                f"User ID provided does not exist [{user_id}]"
            )

        attrs["user"] = user_obj
        attrs["car"] = car_obj
        return attrs
