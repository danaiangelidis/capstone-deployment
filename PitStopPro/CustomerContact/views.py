from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import smtplib


from Jobs.models import Client as Cl
from Invoicing.forms import InvoiceForm
from .models import Messages
from .forms import MessageForm
from .utils import sendSMS

# CARRIERS = {
#     "att": "@mms.att.net",
#     "tmobile": "@tmomail.net",
#     "verizon": "@vtext.com",
#     "sprint": "@messaging.sprintpcs.com"
# }
 
# EMAIL = "PitStopProTeam@gmail.com"
# PASSWORD = "vmoj fuqr ekad klpg"
# Create your views here.
def CustomerContact(request, clientID=None):
    
    clients = Cl.objects.all()
    
    instance = Messages()
    if clientID:
        instance = get_object_or_404(Messages,pk=clientID)
    else:
        instance = Messages()
    form = MessageForm(request.POST or None,instance=instance)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            
    
    context = {'clients': clients}
    return render(request, "customerContact.html", context)

def sendMessage(request, clientID= None):
    # EMAIL = "PitStopProTeam@gmail.com"
    # PASSWORD = "oquj dyov lcri ezmk"
    message = request.POST.get('message')
    instance = Cl()
    if clientID:
        instance = get_object_or_404(Cl,pk=clientID)
        clientNumber = instance.phoneNumber
        if message != None:
            sendSMS(clientNumber,message)
            
    clientINFO = Cl.objects.all()
    context = {'clients': clientINFO, 'clientNumber':clientNumber}
    
    return render(request, "viewMessage.html", context)

def sendToAll(request):
    message = request.POST.get('message')
    instance = Cl.objects.all()
    for number in instance:
        if message != None:
            
            sendSMS(number.phoneNumber,message)
    clientINFO = Cl.objects.all()
    clientNumber = "ALL"
    context = {'clients': clientINFO, 'clientNumber':clientNumber}
    return render(request, "messageAll.html", context)