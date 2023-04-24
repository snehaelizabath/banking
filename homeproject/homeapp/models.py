from django.db import models
from bank.bank import Bank
# Create your models here.
class bank(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()

class registration(models.Model):
    p_name=models.CharField(max_length=100)
    p_DOB=models.DateField()
    p_age=models.CharField(max_length=3)
    p_phonenumber=models.CharField(max_length=10)
    p_email=models.EmailField()
class Movie(models.Model):
    name = models.CharField(max_length=100)
    DOB = models.DateField()
    age = models.CharField(max_length=3)
    phonenumber = models.CharField(max_length=10)
    email = models.EmailField()


    def __str__(self):
        return self.name








