from django.shortcuts import render
from django.db.models import Sum
from .models import Transaction
from datetime import datetime, timedelta
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def earnings_view(request, period):
    today = datetime.today()
    if period == 'weekly':
        start_date = today - timedelta(days=today.weekday())
    elif period == 'monthly':
        start_date = today.replace(day=1)
    elif period == 'quarterly':
        start_month = (today.month - 1) - (today.month - 1) % 3 + 1
        start_date = today.replace(month=start_month, day=1)
    else:
        # Handle incorrect period or set a default
        start_date = today

    earnings = Transaction.objects.filter(date__gte=start_date).aggregate(total_earnings=Sum('amount'))['total_earnings']

    return render(request, 'earnings/earnings_page.html', {
        'earnings': earnings, 
        'period': period  # Add this line to pass 'period' to your template
    })


def download_report(request, period):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    p = canvas.Canvas(response)

    # Example content, customize as needed
    p.drawString(100, 100, "Earnings Report - {}".format(period.capitalize()))

    p.showPage()
    p.save()
    return response
