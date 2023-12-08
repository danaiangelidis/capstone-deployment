# Forms to handle user input when editing Employee
# and payroll information. Forms based on the models
# defined

from django import forms
from .models import Employee, Payroll


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'position', 'bank_account_info']

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = '__all__'
