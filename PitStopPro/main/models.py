from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return "Inventory Query #{}".format(self.id)
    
from django.db import models

# Invoicing

class Invoice(models.Model):
    dateIssued = models.DateTimeField(auto_now_add=True)

    # Labor
    laborHours = models.IntegerField()
    laborRate = models.DecimalField(decimal_places=2 , max_digits=10)

    # Items
    item1Desc = models.TextField()
    item1Price = models.DecimalField(decimal_places=2, max_digits=100000000)
    item1Qty = models.IntegerField()

    item2Desc = models.TextField()
    item2Price = models.DecimalField(decimal_places=2, max_digits=100000000)
    item2Qty = models.IntegerField()

    item3Desc = models.TextField()
    item3Price = models.DecimalField(decimal_places=2, max_digits=100000000)
    item3Qty = models.IntegerField()

    # Totals
    # totalLabor = laborHours*laborRate
    # !!!!!!!!FIGURE THIS ONE OUT!!!!!!!! totalItems = 
    # totalNoTax = totalLabor+totalItems

    # Tax Accounting
    Tax = models.DecimalField(decimal_places=2, max_digits=5)
    # totalPrice = totalNoTax*Tax

    
    def __str__(self):
        return 'Invoice #{}'.format(self.id)
    
class Client(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    email = models.EmailField(max_length=50)
       
class Vehicle(models.Model):
    type = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    plateNumber = models.CharField(max_length=10)

class Company(models.Model):
    name = "Automotive Company"
    address = "123 Address Line Drive"
    city = "Columbia"
    state = "SC"

    #ALLALALALALALAL