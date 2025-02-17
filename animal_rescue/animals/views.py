from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from animals.models import Animals
from animals.serializer import AnimalsSerializer


class AnimalsViewSet(viewsets.ModelViewSet):
    queryset = Animals.objects.all()
    serializer_class = AnimalsSerializer