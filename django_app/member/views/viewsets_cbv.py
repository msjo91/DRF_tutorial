from django.contrib.auth.models import Group
from rest_framework import viewsets

from member.serializers import UserSerializer, GroupSerializer
from member.models import MyUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
