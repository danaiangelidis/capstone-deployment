# Create your views here.
# views.py
from django.shortcuts import render, get_object_or_404, redirect
#from .models import Employee, Payroll
#from .forms import EmployeeForm, PayrollForm
"""
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'html/employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('html/employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'html/employee_detail.html', {'form': form})

def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'html/payroll_list.html', {'payrolls': payrolls})

def payroll_detail(request, payroll_id):
    payroll = get_object_or_404(Payroll, id=payroll_id)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('html/payroll_list')
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'html/payroll_detail.html', {'form': form})
"""
def coming_soon(request):
    return render(request, 'html/coming_soon.html')