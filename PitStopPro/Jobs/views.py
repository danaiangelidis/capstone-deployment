from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.forms import inlineformset_factory
# Create your views here.
def viewJobs(request):
    jobs = Jobs.objects.all()
    context = {'jobs' : jobs}
    return render(request, "jobs.html",context)

def addClient(request):
    if request.method == 'POST':
        clientform = ClientForm(request.POST)
        
        if clientform.is_valid():
            clientform.save()
        
    else:
        clientform = ClientForm()

    if request.method == 'POST':
        vehicleform = VehicleForm(request.POST)
        
        if vehicleform.is_valid():
            vehicleform.save()
            
            return HttpResponseRedirect(reverse('createjobs'))
    else:
        vehicleform = VehicleForm()
    return render(request, 'addClient.html',{'clientform' : clientform, 'vehicleform': vehicleform})
        
def createJob(request):

    if request.method == 'POST':
        form = JobsForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            
            return HttpResponseRedirect(reverse('jobs'))
    else:
        form = JobsForm()
        
            
    
    
    return render(request, 'createjobs.html',{'form' : form})
    