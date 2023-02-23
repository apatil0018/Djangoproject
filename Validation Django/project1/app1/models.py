from django.db import models

# Create your models here.

class Registeration(models.Model):
    eid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mail = models.EmailField()
    password = models.CharField(max_length=40)
    C_password = models.CharField(max_length=40)
