from django.urls import path

from apps.auth_user import apis

app_name = "users"


urlpatterns = [
    path("", apis.UserRegisterViewSet.as_view({"post": "create"}), name="user-list"),
]
