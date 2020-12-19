from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User, Class, Race, Character
from .serializers import UserSerializer, ClassSerializer, RaceSerializer, CharacterSerializer
from rest_framework import viewsets
# from rest_framwork_extensions.mixins import NestedViewSetMixin  (pip install drf-extensions)??


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
