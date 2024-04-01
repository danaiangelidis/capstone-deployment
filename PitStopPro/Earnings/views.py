import matplotlib
matplotlib.use('Agg')

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.template.loader import render_to_string
from io import BytesIO
import base64
from django.core.files.base import ContentFile
from PIL import Image
import matplotlib.pyplot as plt
import io
from django.shortcuts import render
from django.db.models import Sum
from .models import Transaction
from datetime import datetime, timedelta
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch

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
    # Generate the earnings chart
    earningsData = {
        'Week 1': 5000,
        'Week 2': 6000,
        'Week 3': 7000,
        'Week 4': 8000
    }
    labels = list(earningsData.keys())
    values = list(earningsData.values())
    
    buffer = io.BytesIO()
    
    plt.figure(figsize=(8, 4))
    plt.plot(labels, values, marker='o')
    plt.xlabel('Week', fontsize=10, fontweight='bold')
    plt.ylabel('Earnings', fontsize=10, fontweight='bold')
    plt.title('Earnings Over Time', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, fontsize=8)
    plt.yticks(fontsize=8)
    plt.grid(True)
    plt.tight_layout()
    
    plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.1)
    plt.close()
    buffer.seek(0)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    
    p = canvas.Canvas(response)
    
    canvas_width, canvas_height = p._pagesize
    graph_width = min(canvas_width - 2 * inch, 6 * inch)
    graph_height = min(canvas_height - 2 * inch, 3 * inch)
    
    x_position = (canvas_width - graph_width) / 2
    y_position = (canvas_height - graph_height) / 2
    
    p.drawImage(ImageReader(buffer), x_position, y_position, width=graph_width, height=graph_height)
    
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, canvas_height - inch, "Earnings Report - {}".format(period.capitalize()))
    
    
    # img_reader = ImageReader(buffer)
    # img_width, img_height = img_reader.getSize()
    
    # img_str = base64.b64encode(buffer.getvalue()).decode()
    # buffer.close()
    
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    
    # p = canvas.Canvas(response)
    
    # Calculate the appropriate dimensions to fit the graph within the PDF canvas
    # graph_width = min(img_width, canvas_width - 200)
    # graph_height = min(img_height, canvas_height - 200)
    
    # Calculate the positioning to center the graph
    # x_position = (canvas_width - graph_width) / 2
    # y_position = (canvas_height - graph_height) / 2
    
    # Draw the graph on the PDF canvas
    # p.drawImage(img_reader, x_position, y_position, width=graph_width, height=graph_height)
    
    # p.drawString(100, 300, "Earnings Report - {}".format(period.capitalize()))
    
    p.showPage()
    p.save()
    
    # html_content = render_to_string('earnings/earnings_report_with_graph.html', {'img_str': img_str})
    
    # p.drawString(100, 800, "Earnings Report - {}".format(period.capitalize()))
    # p.drawHTMLString(html_content, 100, 700)
    
    
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # p = canvas.Canvas(response)

    # Example content, customize as needed
    # p.drawString(100, 100, "Earnings Report - {}".format(period.capitalize()))

    # p.showPage()
    # p.save()
    return response