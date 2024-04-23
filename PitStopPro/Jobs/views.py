from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required


@login_required
def viewJobs(request):
    jobs = Jobs.objects.all()
    context = {'jobs' : jobs}
    return render(request, "jobs.html",context)

@login_required
def addClient(request):
    if request.method == 'POST':
        clientform = ClientForm(request.POST)
        
        if clientform.is_valid():
            clientform.save()
            return HttpResponseRedirect(reverse('createjobs'))
        
    else:
        clientform = ClientForm()
    return render(request, 'addClient.html',{'clientform' : clientform})

def addVehicle(request):
    if request.method == 'POST':
        vehicleform = VehicleForm(request.POST)
        
        if vehicleform.is_valid():
        
            vehicleform.save()
            
            return HttpResponseRedirect(reverse('createjobs'))
    else:
        vehicleform = VehicleForm()
    return render(request, 'addVechile.html',{ 'vehicleform': vehicleform})
def updateInventory(partName,num):

    for part in partName:
        Inventory.objects.get(partName=part.partName).updateNum(num)

@login_required   
def createJob(request):

    if request.method == 'POST':
        form = JobsForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            updateInventory(form.cleaned_data['parts'],form.cleaned_data['numPart'])

            
            return HttpResponseRedirect(reverse('jobs'))
    else:
        form = JobsForm()
        
    
        
    form.order_fields(field_order=['client', 'vehicle', 'type', 'employee', 'parts'])       
    
    
    return render(request, 'createjobs.html',{'form' : form})

@login_required
def deleteJob(request, jobs_id=None):
    job = Jobs()
    if jobs_id:
        job = get_object_or_404(Jobs, pk=jobs_id)
        job.delete()
    else:
        job = Jobs()
    return HttpResponseRedirect(reverse('jobs'))
    