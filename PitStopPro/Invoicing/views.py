from django.shortcuts import render, redirect, get_object_or_404
from Jobs.models import Invoice
from Jobs.models import Jobs
from Employees.models import Payroll
from .forms import InvoiceForm
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from decimal import Decimal


import io

@login_required
def createInvoice(request):
    invoice = Jobs.objects.all()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('invoicing')
    else:
        
        form = InvoiceForm()
        
    context = {'form' : form}
    return render(request, 'createinvoice.html', context)

@login_required
def viewInvoices(request):
    invoices = Jobs.objects.all()
    context = {'invoices' : invoices}
    return render(request, 'viewinvoices.html', context)

@login_required
def deleteInvoice(request, jobs_id=None):
    job = Jobs()
    if jobs_id:
        job = get_object_or_404(Jobs, pk=jobs_id)
        job.delete()
    else:
        job = Jobs()
    return HttpResponseRedirect(reverse('invoicing'))

@login_required
def downloadInvoice(request, jobs_id=None): 
    invoice = Jobs()
    payroll = Payroll()  

    if jobs_id:
        invoice = get_object_or_404(Jobs, pk=jobs_id)
    else:
        invoice = Jobs()
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{jobs_id}.pdf"'

    page = canvas.Canvas(response)

    # Client Section
    page.setFont("Courier-Bold", 15)
    page.drawString(50, 800, f'{invoice.client.firstName} {invoice.client.lastName}')

    page.setFont("Courier", 12)
    page.drawString(50, 780, f'{invoice.client.address}, {invoice.client.city}, {invoice.client.state}')
    page.drawString(50, 760, f'{invoice.client.phoneNumber}')
    page.drawString(50, 740, f'Vehicle: {invoice.vehicle.year} {invoice.vehicle.make} {invoice.vehicle.model} {invoice.vehicle.type}')
    page.drawString(50, 720, f'Plate Number: {invoice.vehicle.plateNumber}')

    # Items Section
    page.setFont("Courier-Bold", 12)
    background = (229, 229, 229)
    text_margin = 5
    text_height = page._leading

    page.setFillColor(background)
    page.rect(50, 680 - text_height/3, 400, text_height, fill=1)
    page.rect(400, 680 - text_height/3, 100, text_height, fill=1)
    page.rect(450, 680 - text_height/3, 70, text_height, fill=1)

    page.setFillColorRGB(0, 0, 0)
    page.drawString(50 + text_margin, 680, 'Description')
    page.drawString(400 + text_margin, 680, 'Price')
    page.drawString(450 + text_margin, 680, 'Quantity')

    height = 0
    total_items = 0
    for part in invoice.parts.all():
        page.setFont("Courier", 12)
        page.drawString(50 + text_margin, 660 - height, f'{part}')
        page.drawString(400 + text_margin, 660 - height, f'{part.price}')
        page.drawString(450 + text_margin, 660 - height, f'{invoice.numPart}')
        height += 20
        total_items+=part.price*invoice.numPart

    employee_name = 'None'
    for employee in invoice.employee.all():
        employee_name = employee.name
    page.drawString(50, 640 - height, f'Employee: {employee_name}')

    total_labor = 0
    total_hours = 0
    for rate in invoice.type.all():
        for part in invoice.parts.all():
            total_hours = rate.est_time
            total_labor = rate.laborRate*rate.est_time

    page.drawString(50, 620 - height, f'Total Labor: ${total_labor}')
    page.drawString(50, 600 - height, f'Total Labor Hours: {total_hours}')
    page.drawString(50, 580 - height, f'Total Items: ${total_items}')

    x_start = 50
    x_end = 530
    y = 560 - height
    page.line(x_start, y, x_end, y)

    total_b4_tax = total_labor + total_items
    page.drawString(50, 540 - height, f'Total Before Tax: ${total_b4_tax}')

    tax_rate = Decimal('0.06')
    tax = total_b4_tax*tax_rate
    page.drawString(50, 520 - height, f'Tax: ${tax}')

    page.setFont("Courier-Bold", 15)
    total_total = tax+total_b4_tax
    page.drawString(50, 500 - height, f'Subtotal: ${total_total}')

    page.showPage()
    page.save()

    return response