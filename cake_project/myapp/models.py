from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    f_name = models.CharField(max_length=80)
    l_name = models.CharField(max_length=80)
    contact = models.CharField(max_length=80)
    address = models.CharField(max_length=500)
    otp = models.IntegerField(default=1234)



class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=1000)

