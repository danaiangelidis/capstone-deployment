# Create your views here.
# views.py
from http.client import HTTPResponse 
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from .models import Payroll
from Jobs.models import Employee
from .forms import EmployeeForm, PayrollForm
from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_payroll') # Redirects back to the same page
    else:
        form = EmployeeForm()

    employees = Employee.objects.all() # Or any other query to fetch employee data
    return render(request, 'Employees/employee_list.html', {'employees': employees, 'form': form})

@require_POST
@login_required
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    return redirect('employee_list') # Redirect to the employee list or another appropriate page

@login_required
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    print(employee)
    payroll_info = Payroll.objects.filter(employee=employee).first() # Get the associated payroll info
    
    if not employee_id:
        return HTTPResponse("Invalid Employee ID")
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            #return redirect('employees/employee_list', employee_id=employee.id) # Redirect to the employee list or another appropriate page
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    
    context = {
        'form': form,
        'employee': employee,
        'payroll_info': payroll_info # Add payroll_info to the context
    }
    return render(request, 'Employees/employee_detail.html', context)

#View for listing all payroll entries
@login_required
def payroll_list(request):
    payroll_entries = Payroll.objects.all() # Get all payroll entries from the database
    return render(request, 'Employees/payroll_list.html', {'payroll_entries': payroll_entries})

#View for viewing and editing payroll details for a specific employee
@login_required
def payroll_detail(request, payroll_id):
    payroll_entry = get_object_or_404(Payroll, pk=payroll_id)
    
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll_entry)
        if form.is_valid():
            form.save()
            # Redirect to payroll list or a confirmation page after saving
            return redirect('payroll_list')
    else:
        form = PayrollForm(instance=payroll_entry)
    
    return render(request, 'Employees/payroll_detail.html', {'form': form})

@login_required
def addPayroll(request):
    if request.method == 'POST':
        payrollform = PayrollForm(request.POST)
        
        if payrollform.is_valid():
        
            payrollform.save()
            
            return HttpResponseRedirect(reverse('employee_list'))
    else:
        payrollform = PayrollForm()
    return render(request, 'Employees/addPayroll.html',{ 'payrollform': payrollform})


