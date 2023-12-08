"""
URL configuration for PitStopPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Home import views as homeViews
from Calendar import views as calendarViews
from Inventory import views as inventoryViews
from Employees import views as employeeViews
from Invoicing import views as invoiceViews
from Authentication import views as authViews
from userSettings import views as settingViews
from Pricing import views as pricingViews

urlpatterns = [
    path("", authViews.signin, name = "login/"),
    path("login/", authViews.signin, name = "login/"),
    path("",include('django.contrib.auth.urls')),
    path("login/",include('django.contrib.auth.urls')),
    path("signup/", authViews.signup, name = "signup/"),
    path("settings/", settingViews.settings, name = "settings/"),
    path("home/", homeViews.Home,name="home"),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('calendar/', calendarViews.CalendarView.as_view(), name='calendar'),
    path('event/new/', calendarViews.event, name='event_new'),
    path('event/edit/(?P<event_id>\d+)/', calendarViews.event, name='event_edit'),
    path('inventory/', inventoryViews.inventory, name='inventory'),
    path('inventory/new/',inventoryViews.new_inventory,name="new_inventory"),
    path('inventory/edit/(?P<inventory_id>\d+)',inventoryViews.new_inventory,name="edit_inventory"),
    path('inventory/delete/(?P<inventory_id>\d+)',inventoryViews.delete_inventory,name="delete_inventory"),
    path('employees/', employeeViews.employee_list, name='employee_list'),
    path('<int:employee_id>/', employeeViews.employee_detail, name='employee_detail'), # THIS ONE
    path('payroll/', employeeViews.payroll_list, name='payroll_list'),
    path('payroll/<int:payroll_id>/', employeeViews.payroll_detail, name='payroll_detail'),
    path('employees/delete/<int:employee_id>/', employeeViews.delete_employee, name='delete_employee'),
    path('createinvoice/', invoiceViews.createInvoice, name='createinvoice'),
    path('invoicing/', invoiceViews.viewInvoices, name='invoicing'),
    path('pricing/', pricingViews.viewPricing, name='pricing'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
