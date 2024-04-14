from django.db import models
from users.models import User

# Create your models here.
class Scale(models.Model):

    date = models.DateField(max_length=64)
    range = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

