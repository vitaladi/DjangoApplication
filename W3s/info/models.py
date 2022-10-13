from django.db import models

class Objectif(models.Model):
    name= models.CharField(max_length=255)
    content = models.CharField(max_length=516)
# Create your models here.
