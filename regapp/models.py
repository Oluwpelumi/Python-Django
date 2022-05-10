from django.db import models

# Create your models here.

class registration(models.Model):
    firstname  = models.CharField(max_length=50)
    lastname  = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    religion = models.CharField(max_length=30)
