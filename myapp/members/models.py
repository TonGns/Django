from django.db import models

# Create your models here.
class Members(models.Model):
    emp_id = models.CharField(max_length=3, primary_key=True)
    image = models.ImageField(upload_to='images')
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=5)
    age = models.CharField(max_length=2)

