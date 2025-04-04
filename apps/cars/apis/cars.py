from rest_framework import permissions, response, viewsets
from rest_framework.decorators import action

from apps.cars.models.cars import Car
from apps.cars.serializers import CarSerializer, CarSummarySerializer

__all__ = [
    "CarViewSet",
]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = "pk"
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=True, methods=["get"])
    def make_summary(self, request, make_name):
        cars = Car.objects.filter(make=make_name)
        data = CarSummarySerializer(cars, many=True).data
        return response.Response(data)
