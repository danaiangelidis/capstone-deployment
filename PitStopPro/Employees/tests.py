# Create your tests here.
# employees/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Employee, Payroll
from .forms import EmployeeForm, PayrollForm
from django.utils import timezone

class EmployeesTestCase(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.employee = Employee.objects.create(
            name="John Doe",
            email="john@example.com",
            position="Manager",
            bank_account_info="123456789",
        )

        self.payroll = Payroll.objects.create(
            employee=self.employee,
            salary=5000.00,
            pay_period=timezone.now(),
        )

    def test_employee_form(self):
        # Test EmployeeForm
        form_data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'position': 'Developer',
            'bank_account_info': '987654321',
        }
        form = EmployeeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_payroll_form(self):
        # Test PayrollForm
        form_data = {
            'employee': self.employee.id,
            'salary': 6000.00,
            'pay_period': timezone.now(),
        }
        form = PayrollForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_employee_detail_view(self):
        # Test the employee_detail view
        response = self.client.get(reverse('employee_detail', args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')  # Check if the employee's name is present in the response

    def test_payroll_detail_view(self):
        # Test the payroll_detail view
        response = self.client.get(reverse('payroll_detail', args=[self.payroll.id]))
        self.assertEqual(response.status_code, 200)

        # Print the content of the response for debugging
        print(response.content.decode('utf-8'))

        # Check if the form input for salary is present in the response
        self.assertContains(response, '<input type="text" id="salary1" name="salary1" placeholder="Enter salary for John Doe">', html=True)