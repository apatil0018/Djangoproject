from django.db import models

# Create your models here.

class Student(models.Model):
    sid=models.IntegerField()
    name=models.CharField(max_length=100)
    FMT = models.BooleanField(default=True)

   

    def __str__(self):
        return self.name

