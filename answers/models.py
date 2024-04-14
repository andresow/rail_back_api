from django.db import models
from questions.models import Questions
from users.models import User

# Create your models here.
class Answers(models.Model):


    answer = models.CharField(max_length=200)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE,null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return self.answer