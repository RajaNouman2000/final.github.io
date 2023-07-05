from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
