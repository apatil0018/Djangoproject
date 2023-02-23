from unicodedata import name
from django.db import models

# Create your models here.

class Employee(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phoneNo = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class AddressDetails(models.Model):
    h_no = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="addressDetails")

    def __str__(self):
        return self.street