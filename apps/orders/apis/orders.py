from rest_framework import permissions, viewsets

from apps.auth_user.models import User
from apps.cars.models import Car
from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer

__all__ = [
    "OrderViewSet",
]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
