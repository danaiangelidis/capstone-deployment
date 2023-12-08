from django import forms
from .models import Inventory
from django.forms import ModelForm

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super(InventoryForm,self).__init__(*args,**kwargs)