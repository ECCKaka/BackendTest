from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from backendTest.models import *
from .serializers import *

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
    )

# this is ListAPIView, it allows user to view all data in one model
class UserViewSet(ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# this is CreateAPIView, in order to create a log, it needs this api
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# this is RetrieveAPIView, we could pass in primary key to view one user info
class OneUserAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
