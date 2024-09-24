from django.db import models

# Create your models here.

class Employee(models.Model):
    nombre1 = models.CharField(max_length=50)
    email1 = models.CharField(max_length=50)
    fono = models.CharField(max_length=25)

