from django.db import models

# Create your models here.

class Student(models.Model):
    rn = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.rn}--{self.fname}--{self.lname}--{self.city}'
    
    



class Courses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    courseName = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.student}--{self.courseName}'







