from django.urls import path
# from . import views
from.views import employee_list, employee_detail, payroll_list, payroll_detail, delete_employee

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('<int:employee_id>/', employee_detail, name='employee_detail'), # THIS ONE
    path('payroll/', payroll_list, name='payroll_list'),\
    path('payroll/<int:payroll_id>/', payroll_detail, name='payroll_detail'),
    path('employees/delete/<int:employee_id>/', delete_employee, name='delete_employee'),
]