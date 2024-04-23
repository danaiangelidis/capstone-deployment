from django import forms
from Jobs.models import Inventory
from django.forms import ModelForm

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['stockNumber', 'quantity', 'description', 'type', 'partName', 'price']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative.")
        return quantity

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price