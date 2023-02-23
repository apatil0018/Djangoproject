from django.db import models

# Create your models here.

STATE_CHOICES = ((
    ('Bihar','Bihar'),
    ('Jarkhand','Jarkhand'),
    ('Delhi','Delhi'),
    ('Maharashtra','Maharashtra'),
    ('Gujarat','Gujarat'),
    ('Uttarpradesh','Uttarpradesh'),
    ('HimachalPradesh','HimachalPradesh'),
    ('Goa','Goa'),
    ('Bingaluru','Bingaluru'),
    ('Rajasthan','Rajasthan'),
))

class Profile(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False,auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='pimage', blank=True)
    rdoc = models.FileField(upload_to='rdocs', blank=True)
    
    



