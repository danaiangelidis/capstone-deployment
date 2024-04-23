import matplotlib
matplotlib.use('Agg')

from .forms import EarningsForm
from django.http import HttpResponse, JsonResponse
from reportlab.pdfgen import canvas
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
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
import json


def earnings_view(request, period):
    form = EarningsForm(request.POST or None)
    if form.is_valid():
        num_months = form.cleaned_data['num_months']
        earnings_per_month = form.cleaned_data['earnings_per_month']
        earnings_data = {f'Month {i + 1}': earnings_per_month for i in range(num_months)}
        request.session['graph_labels'] = list(earnings_data.keys())
        request.session['graph_values'] = list(earnings_data.values())

    labels = request.session.get('graph_labels', ['Month 1'])
    values = request.session.get('graph_values', [0])

    context = {
        'form': form,
        'labels': json.dumps(labels),
        'values': json.dumps(values),
    }

    return render(request, 'Earnings/earnings_page.html', context)


@csrf_exempt
def update_graph(request):
    try:
        data = json.loads(request.body)
        earnings = data.get('earnings')
        labels = list(earnings.keys())
        values = [float(val) for val in earnings.values()]

        request.session['graph_labels'] = labels
        request.session['graph_values'] = values
        
        return JsonResponse({'labels': labels, 'values': values})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def retrieve_current_session_data(request):
    labels = request.session.get('graph_labels', [])
    values = request.session.get('graph_values', [])
    return labels, values

def download_report(request, period):
    today = datetime.today()
    if period == 'current':
        labels, values = retrieve_current_session_data(request)
    elif period == 'weekly':
        start_date = today - timedelta(days=today.weekday())
    elif period == 'monthly':
        start_date = today.replace(day=1)
    elif period == 'quarterly':
        start_month = (today.month - 1) - (today.month - 1) % 3 + 1
        start_date = today.replace(month=start_month, day=1)
    else:
        start_date = today
    # Generate earnings chart
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    p = canvas.Canvas(response)

    #earningsData = {
    #    'Week 1': 5000,
    #    'Week 2': 6000,
    #    'Week 3': 7000,
    #    'Week 4': 8000
    #}
    # labels = list(earningsData.keys())
    # values = list(earningsData.values())
    
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
    for label, value in zip(labels, values):
        p.drawString(100, y_position, f"{label}: ${value}")
        y_position -= 20
    p.showPage()
    p.save()
    return response