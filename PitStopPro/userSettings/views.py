from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.
def settings(request):
    if request.method == "POST":
        logout(request)
        return redirect('login/')
    else:   
        return render(request, "userSettings.html") 
