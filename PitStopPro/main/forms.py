from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ["name","quantity",]
        labels = {"partName":"Part Name","quantity":"Quantity",}