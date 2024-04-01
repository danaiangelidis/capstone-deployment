from django.shortcuts import render, redirect
from Jobs.models import Invoice
from Jobs.models import Jobs
from .forms import InvoiceForm

def createInvoice(request):
    jobs = Jobs.objects.all()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('invoicing') 
    else:
        
        form = InvoiceForm()
        
    context = {'form' : form}
    return render(request, 'createinvoice.html', context)

def viewInvoices(request):
    invoices = Jobs.objects.all()
    context = {'invoices' : invoices}
    return render(request, 'viewinvoices.html', context)