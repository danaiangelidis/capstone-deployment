from django.db import models

# Create your models here.
# models.py

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    bank_account_info = models.CharField(max_length=255, default='Default Value')
    bank_account_info = models.CharField(max_length=255, blank=True, null=True, help_text="Information for wire transfer")
    # Add other employee information fields here
    
    def __str__(self):
        return self.name
    
    
class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    pay_period = models.DateField()
    # Add other payroll-related fields here
    
    def __str__(self):
        return f"{self.employee.name} - {self.pay_period}"