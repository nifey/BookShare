from django.db import models
class Person(models.Model):
    email  = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    password = models.CharField(max_length=250)#we can store the hashed password here
# Create your models here.
