from django.shortcuts import render
from rest_framework import viewsets
from .serializer import AnswersSerializer
from .models import Answers
# Create your views here.
class AnswersView(viewsets.ModelViewSet):

    serializer_class= AnswersSerializer
    queryset = Answers.objects.all()