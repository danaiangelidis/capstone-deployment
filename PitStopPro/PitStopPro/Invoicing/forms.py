from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InvoiceForm,self).__init__(*args, **kwargs)