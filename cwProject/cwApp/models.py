from django.db import models

# Create your models here.

from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=10)
    breed = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    gender = models.CharField(max_length=7)

class Question2(models.Model):
    username = models.CharField(max_length=15)
    realName = models.CharField(max_length=20)
    accountNumber = models.DecimalField(max_digits=10, decimal_places=3)
    balance = models.DecimalField(max_digits=10, decimal_places=3)