from rest_framework import serializers

from apps.cars.models import Car

__all__ = [
    "CarSerializer",
    "CarSummarySerializer",
]


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields: tuple[str, ...] = (
            "model",
            "year",
            "speed",
        )
