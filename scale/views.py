from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ScaleSerializer
from .models import Scale
# Create your views here.
class ScaleView(viewsets.ModelViewSet):

    serializer_class= ScaleSerializer
    queryset = Scale.objects.all()