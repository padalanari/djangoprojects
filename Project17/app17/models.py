from django.db import models

# Create your models here.
class StudentDetailsModel(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to='Student_images')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)