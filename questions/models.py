from django.db import models

# Create your models here.
class Questions(models.Model):

    CHOICES = [('unique_selection', 'Unica seleccion'), ('selector', 'Selector'), ('open', 'Abierta')]

    title = models.CharField(max_length=200)
    question_type = models.CharField(max_length=64, choices=CHOICES)
    stage = models.IntegerField()