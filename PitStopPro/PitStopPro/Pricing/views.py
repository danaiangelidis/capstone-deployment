from django.shortcuts import render, redirect

def viewPricing(request):
    return render(request, 'customPricing.html')