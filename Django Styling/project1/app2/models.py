from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.IntegerField()
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=40)
    
