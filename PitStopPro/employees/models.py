from django.db import models

# Create your models here.
# models.py
"""
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Add other employee information fields here
    class Meta:
        app_label = 'employees'
class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other payroll-related fields here
"""