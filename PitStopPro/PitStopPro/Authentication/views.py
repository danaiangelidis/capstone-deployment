from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

# view for directing the signup page form when a new account is created or the page is loaded
def signup(request):
    if request.method == "POST":
        username = request.POST['email']
        first_name = request.POST["fname"]
        last_name = request.POST['lname']
        email = request.POST['email']
        phone_number = request.POST['phonenum']
        buisness_name = request.POST['bname']
        password = request.POST['password']
        confirm_password = request.POST.get('pass2')
    # exception catches for invalid inputs on creation form
        
        # test to ensure a valid email input
        try:
            validate_email(email)
        except ValidationError:
            error_message = "Please enter a valid email address."
            return render(request, "signup.html", {"error_message": error_message})
        
        # test to ensure email used in creation is not already associated with an account 
        if User.objects.filter(email=email).exists():
            error_message = "This email is already registered."
            return render(request, "signup.html", {"error_message": error_message})
        # test to ensure that password matches confirmed password field
        if password != confirm_password:
            error_message = "Passwords do not match."
            return render(request, "signup.html", {"error_message": error_message})
        # test to ensure password is atleast 8 characters long
        if len(password) < 8:
            error_message = "Password should be at least 8 characters long."
            return render(request, "signup.html", {"error_message": error_message})
        # test to ensure password has atleast one Uppercase character
        if not re.search(r'[A-Z]', password):
            error_message = "Password should contain at least one uppercase letter."
            return render(request, "signup.html", {"error_message": error_message})
        # test to ensure the password contains atleast one number
        if not re.search(r'\d', password):
            error_message = "Password should contain at least one number."
            return render(request, "signup.html", {"error_message": error_message})

        #creates a new user using form data in the database
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        #redirect to login page upon successful save of new user 
        return redirect('login/')
    else:
        #when a blank page request without a post ,load page
        return render(request, "signup.html", {})

# view for sign in page
def signin(request):
   
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        # ensures both fields are populated in form
        if not email or not password:
            error_message = "Please provide both email and password."
            return render(request, "login.html", {"error_message": error_message})
        #ensures user exists and password matches
        user = authenticate(request, username=email, password=password)
        # if passes authenticate, user is logged in an redirected to home
        if user is not None:
            login(request, user)
            return redirect('home')
        # if invalid email or password, display error and return to login page
        else:
            error_message = "Invalid email or password."
            return render(request, "login.html", {"error_message": error_message})

    return render(request, "login.html")
# loads the privacy policy page
def privacy_policy(request):
    return render(request, 'privacypolicy.html')
# loads the terms and conditions page
def terms_and_conditions(request):
    return render(request, 'termsandconditions.html')