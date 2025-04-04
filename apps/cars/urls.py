from django.urls import path

from apps.cars import apis

app_name = "cars"


urlpatterns = [
    path(
        "", apis.CarViewSet.as_view({"get": "list", "post": "create"}), name="car-list"
    ),
    path(
        "<int:pk>",
        apis.CarViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="car-details",
    ),
    path(
        "models/<str:make_name>",
        apis.CarViewSet.as_view({"get": "make_summary"}),
        name="make-summary",
    ),
]
