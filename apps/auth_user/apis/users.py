from rest_framework.viewsets import ModelViewSet

from apps.auth_user.models import User
from apps.auth_user.serializers import UserRegisterSerializer


class UserRegisterViewSet(ModelViewSet):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
