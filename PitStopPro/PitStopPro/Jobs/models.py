from django.db import models
from Inventory.models import Inventory

import uuid
# Create your models here.



class Client(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phoneNumber = models.CharField(max_length=10)
    clientID = models.UUIDField(primary_key = True, default=uuid.uuid4,editable=False)

    def __str__(self):
        return '{} {}'.format(self.firstName, self.lastName) 
class Vehicle(models.Model):
    type = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    plateNumber = models.CharField(max_length=30)
    owner = models.ForeignKey(Client, blank=True, null=True,on_delete=models.CASCADE)
    

    def __str__(self):
        
        return '{} {} {}'.format(self.owner ,self.make, self.model)
# class Inventory(models.Model):
#     stockNumber = models.CharField(max_length=200)
#     quantity = models.IntegerField()
#     description = models.CharField(max_length=200)
#     type = models.CharField(max_length=200)
#     partName = models.CharField(max_length=200)
#     price = models.IntegerField()
    
#     def __str__(self):
#         return '{} id: {}'.format(self.partName, self.stockNumber) 

class Diagnosis(models.Model):
    name = models.CharField(max_length=50)
    est_time = models.IntegerField()
    laborRate = models.DecimalField(decimal_places=2 , max_digits=1000)
    
    def __str__(self):
        return '{} '.format(self.name) 
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    employeeID = models.UUIDField(primary_key = True, default=uuid.uuid4,editable=False)
    
    def __str__(self):
        return 'Staff: {}'.format(self.name) 
    
class Jobs(models.Model):
    client = models.ForeignKey(Client,blank=True,null=True,on_delete=models.PROTECT)
    parts = models.ManyToManyField(Inventory, blank=True)
    numPart = models.IntegerField(default=0)
    type = models.ManyToManyField(Diagnosis, blank=True)
    employee = models.ManyToManyField(Employee, blank=True)
    vehicle = models.ForeignKey(Vehicle,blank=True,null=True,on_delete=models.PROTECT)
    
    def __str__(self):
        return '{} {} '.format(self.vehicle, self.client) 
    
class Invoice(models.Model):
    invoice = models.ManyToManyField(Jobs, blank=True) 
    

    
    
    