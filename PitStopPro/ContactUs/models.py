from django.db import models
# Create your models here.
class Contact(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=12)
    company = models.CharField(max_length=30)
    message = models.CharField(max_length=500)
    
