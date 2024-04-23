from django.shortcuts import render
from Jobs.models import Jobs
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Customers(request):
    customers = Jobs.objects.all()
    name_counts = {}
    for customer in customers:
        name = f"{customer.client.firstName} {customer.client.lastName}"
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    context = {'customers': customers, 'name_counts': name_counts}
    return render(request, 'customers.html', context)

