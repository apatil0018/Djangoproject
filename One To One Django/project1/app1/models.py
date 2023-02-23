from django.db import models

# Create your models here.

class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pid}--{self.fname}{self.lname}'
    


class Adhar(models.Model):
    person = models.OneToOneField(Person,on_delete=models.CASCADE)
    adharno = models.IntegerField()

    def __str__(self):
        return f'{self.person}{self.adharno}'
    

