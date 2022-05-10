from django.db import models

# Create your models here.

class Service(models.Model):
 
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    tag = models.TextField()
    offer1 = models.BooleanField(default=False)
    offer2 = models.BooleanField(default=False)
    offer3 = models.BooleanField(default=False)

"""
class Service2:
    id : int
    price : int
    img : str
    tag : str

class Service3:
    id : int
    price : int
    img : str
    tag : str  
"""