from django.db import models


# Create your models here.
class Admission(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.TextField()
    email = models.EmailField(max_length=70,blank=True,unique=True)
    dob = models.DateField()
    address = models.CharField(max_length=500)
    place = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    
class Placements(models.Model):
    images = models.ImageField()
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ['-id'] 

