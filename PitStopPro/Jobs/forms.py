from django import forms
from Inventory.models import Inventory
from .models import *
from django.forms import ModelForm


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super(InventoryForm,self).__init__(*args,**kwargs)
        
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('type','make','model','year','plateNumber')
    
        
class ClientForm(forms.ModelForm):
    class Meta:
        model =  Client
        fields = '__all__'
        
class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super(DiagnosisForm,self).__init__(*args,**kwargs)
        
class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
