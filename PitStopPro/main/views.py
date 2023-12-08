from django.shortcuts import render
from .models import Inventory
from .forms import InventoryForm

from django.shortcuts import render, redirect
from .models import Invoice

def index(request):
    return render(request, 'html/index.html')

def createInvoice(request):
    return render(request, 'html/createinvoice.html')

def viewInvoices(request):
    invoices = Invoice.objects.all()
    context = {'invoices' : invoices}
    return render(request, 'html/viewinvoices.html', context)

def calender(request):
    return render(request, 'html/calender.html')

def inventory(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InventoryForm()
    return render(request, "html/inventory.html",{'form':form})