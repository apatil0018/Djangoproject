from django.db import models

# Create your models here.
class Company(models.Model):
    info= models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.info

class Workexp(models.Model):
    cmp_name = models.CharField(max_length=100)
    fromdate = models.DateField()
    todate = models.DateField()
    address = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='workexp')

class Qualification(models.Model):
    qualificationName = models.CharField(max_length=100)
    fromdate = models.DateField()
    todate = models.DateField()
    percentage = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="qualifications")

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="projects")



    

