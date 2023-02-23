from django.db import models

# Create your models here.

class Orders(models.Model):
    o_id = models.IntegerField(primary_key=True)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    amt = models.FloatField()
    mail = models.EmailField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.f_name



