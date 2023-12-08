from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 


# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST['email']
        first_name = request.POST["fname"]
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username = username, email = email, password = password ,first_name = first_name, last_name = last_name)
        user.save()
        return redirect('login/')
    else:
        return render(request, "signup.html",{})  

def signin(request): 
    if request.method == "POST":
         email = request.POST["email"]
         password = request.POST["password"]
         user = authenticate(request, username = email, password = password)
         if user is not None:
            login(request, user)
            return redirect('home')
    
    return render(request, "login.html",{})