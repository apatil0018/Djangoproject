from django.db import models

# Create your models here.

class Employee(models.Model):
    regid = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phoneNo = models.CharField(max_length=12)
    photo = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name

class AddressDetails(models.Model):
    h_no = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="addressDetails")

    def __str__(self):
        return self.street


class Workexp(models.Model):
    cmp_name = models.CharField(max_length=100)
    fromdate = models.DateField()
    todate = models.DateField()
    address = models.CharField(max_length=200)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='workexp')

class Qualification(models.Model):
    qualificationName = models.CharField(max_length=100)
    fromdate = models.DateField()
    todate = models.DateField()
    percentage = models.FloatField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="qualifications")

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="projects")



    



