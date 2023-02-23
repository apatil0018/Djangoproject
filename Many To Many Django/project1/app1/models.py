from django.db import models

# Create your models here.

class Owners(models.Model):
    oid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        return self.fname

class Cars(models.Model):
    cid = models.ManyToManyField(Owners)
    year =models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)


    def __str__(self):
        return self.year



    