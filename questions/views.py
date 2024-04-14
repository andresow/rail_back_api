from django.shortcuts import render
from rest_framework import viewsets
from .serializer import QuestionsSerializer
from .models import Questions
# Create your views here.
class QuestionsView(viewsets.ModelViewSet):

    serializer_class= QuestionsSerializer
    queryset = Questions.objects.all()