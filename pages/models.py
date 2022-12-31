from django.db import models

# Create your models here.
class UserInputs(models.Model):
    initialState = models.CharField(max_length=20)
    lastState = models.CharField(max_length=20)
