from django.db import models

class Invoice(models.Model):
    # dateIssued = models.DateTimeField(auto_now_add=True)

    # Company Info
    CompanyName = "Automotive Company"
    companyAddress = "123 Address Line Drive"
    companyCity = "Columbia"
    companyState = "SC"

    # Client Info
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    # Vehicle Info
    type = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    plateNumber = models.CharField(max_length=30)

    # Labor
    laborHours = models.IntegerField()
    laborRate = models.DecimalField(decimal_places=2 , max_digits=1000)

    # Items
    item1Desc = models.TextField()
    item1Price = models.DecimalField(decimal_places=2, max_digits=1000)
    item1Qty = models.IntegerField()

    item2Desc = models.TextField()
    item2Price = models.DecimalField(decimal_places=2, max_digits=1000)
    item2Qty = models.IntegerField()

    item3Desc = models.TextField()
    item3Price = models.DecimalField(decimal_places=2, max_digits=1000)
    item3Qty = models.IntegerField()

    # Tax Accounting
    Tax = models.DecimalField(decimal_places=2, max_digits=5)
    totalPrice = models.DecimalField(decimal_places=2, max_digits=1000)

    # Totals
    totalLabor = models.DecimalField(decimal_places=2, max_digits=1000)
    totalItems = models.DecimalField(decimal_places=2, max_digits=1000)
    totalNoTax = models.DecimalField(decimal_places=2, max_digits=1000)
    
    def __str__(self):
        return 'Invoice #{}'.format(self.id) 