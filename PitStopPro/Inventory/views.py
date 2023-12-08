from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
    #IMMPORTED MODELS
from .models import Inventory
from .forms import InventoryForm
from .models import *
# Create your views here.
def inventory(request,inventory_id=None):
    instance = Inventory()
    if inventory_id:
        instance = get_object_or_404(Inventory,pk=inventory_id)
    else:
        instance = Inventory()
    form = InventoryForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    all_inventory = Inventory.objects.all
    return render(request, "html/inventory.html",{'all':all_inventory})
def new_inventory(request,inventory_id=None):
    instance = Inventory()
    if inventory_id:
        instance = get_object_or_404(Inventory,pk=inventory_id)
        
    else:
        instance = Inventory()
    form = InventoryForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('inventory'))
    return render(request, "html/new_inventory.html",{'form':form})
def delete_inventory(request,inventory_id=None):
    instance = Inventory()
    if inventory_id:
        instance = get_object_or_404(Inventory,pk=inventory_id)
        instance.delete()  
    else:
        instance = Inventory()
    return HttpResponseRedirect(reverse('inventory'))