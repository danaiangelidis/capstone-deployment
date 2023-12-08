from django.urls import path
from . import views

urlpatterns = [
    #path('employees/', views.employee_list, name='employee_list'),
    #path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    #path('payroll/', views.payroll_list, name='payroll_list'),
    #path('payroll/<int:payroll_id>/', views.payroll_detail, name='payroll_detail'),
    path('employees/', views.coming_soon, name='coming_soon'),
]