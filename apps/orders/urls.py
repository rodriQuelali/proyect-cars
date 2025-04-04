from django.urls import path

from apps.orders import apis

app_name = "orders"


urlpatterns = [
    path(
        "",
        apis.OrderViewSet.as_view({"get": "list", "post": "create"}),
        name="order-list",
    ),
    path(
        "<int:pk>",
        apis.OrderViewSet.as_view({"get": "retrieve", "patch": "partial_update"}),
        name="order-details",
    ),
]
