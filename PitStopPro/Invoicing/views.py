from django.shortcuts import render, redirect
from .models import Invoice
from .forms import InvoiceForm

def createInvoice(request):
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
    invoices = Invoice.objects.all()
    context = {'invoices' : invoices}
    return render(request, 'viewinvoices.html', context)