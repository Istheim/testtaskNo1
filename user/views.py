from rest_framework import viewsets

from user.models import User
from user.serliazers import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    serializers_class = UsersSerializer
    queryset = User.objects.all()