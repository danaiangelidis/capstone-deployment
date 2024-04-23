from django.shortcuts import render, redirect

# Create your views here.
def Home(request):
    return render(request, "home.html")
