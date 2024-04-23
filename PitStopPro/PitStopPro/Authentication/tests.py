from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
# test for signup page's error checking features 
class SignupFormTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup/')  
    
    # test user signup feature with a valid set of user data
    def test_signup_form_with_valid_data(self):
        response = self.client.post(self.signup_url, {
            'email': 'test@example.com',
            'fname': 'John',
            'lname': 'Doe',
            'password': 'Password123',
            'pass2': 'Password123'
        })
        self.assertRedirects(response, reverse('login/'))  
        self.assertTrue(User.objects.filter(email='test@example.com').exists())
    
    # test signup with a bad user data set to ensure error catching
    def test_signup_form_with_invalid_email(self):
        response = self.client.post(self.signup_url, {
            'email': 'invalid_email',
            'fname': 'John',
            'lname': 'Doe',
            'password': 'Password123',
            'confirm_password': 'Password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'Please enter a valid email address.')
   
    # test signup with an existing email to ensure duplicate check
    def test_signup_form_with_existing_email(self):
        User.objects.create_user(username='existinguser', email='existing@example.com', password='existingpassword')
        response = self.client.post(self.signup_url, {
            'email': 'existing@example.com',
            'fname': 'John',
            'lname': 'Doe',
            'password': 'Password123',
            'pass2': 'Password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'This email is already registered.')
    
    # test signup with mismatched password fields
    def test_signup_form_with_mismatched_passwords(self):
        response = self.client.post(self.signup_url, {
            'email': 'test@example.com',
            'fname': 'John',
            'lname': 'Doe',
            'password': 'Password123',
            'pass2': 'MismatchedPassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'Passwords do not match.')
    # tests minimum password length check with a bad input
    def test_signup_form_with_short_password(self):
        response = self.client.post(self.signup_url, {
            'email': 'test@example.com',
            'fname': 'John',
            'lname': 'Doe',
            'password': 'Short',
            'pass2': 'Short'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'Password should be at least 8 characters long.')
    
    # test password capital letter requirement check with a bad input
    def test_signup_form_with_password_missing_uppercase(self):
        response = self.client.post(self.signup_url, {
            'email': 'test@example.com',
            'fname': 'John',
            'lname': 'Doe',
            'password': 'password123',
            'pass2': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'Password should contain at least one uppercase letter.')

    # test password number requirement error check with bad input
    def test_signup_form_with_password_missing_number(self):
        response = self.client.post(self.signup_url, {
            'email': 'test@example.com',
            'fname': 'John',
            'lname': 'Doe',
            'password': 'PasswordABC',
            'pass2': 'PasswordABC'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, 'Password should contain at least one number.') 

#tests for the login page's error checking features
class LoginTests(TestCase):
    #sets up a mock user to user for the authentication checks
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login/')  
        self.user = User.objects.create_user(username='testuser@example.com', email='testuser@example.com', password='testpassword')
    # tests the login with the good login input
    def test_login_with_valid_credentials(self):
        response = self.client.post(self.login_url, {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        })
        self.assertRedirects(response, reverse('home')) 
        self.assertTrue(response.wsgi_request.user.is_authenticated)
    # tests the login with a bad email input to ensure error is caught
    def test_login_with_invalid_email(self):
        response = self.client.post(self.login_url, {
            'email': 'invaliduser@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)
    # tests the login with an invalid password input to ensure error is caught
    def test_login_with_invalid_password(self):
        response = self.client.post(self.login_url, {
            'email': 'testuser@example.com',
            'password': 'invalidpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)
   
    # tests login with an empty email field to ensure error is caught
    def test_login_with_empty_email(self):
        response = self.client.post(self.login_url, {
            'email': '',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)
    # tests the login with an empty password field to ensure error is caught
    def test_login_with_empty_password(self):
        response = self.client.post(self.login_url, {
            'email': 'testuser@example.com',
            'password': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)