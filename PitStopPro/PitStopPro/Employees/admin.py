from django.contrib import admin
from Jobs.models import Employee
from .models import Payroll
# Register your models here.
admin.site.register(Employee)
admin.site.register(Payroll)