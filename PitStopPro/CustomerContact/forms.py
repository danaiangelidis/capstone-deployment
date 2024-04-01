from django import forms
from .models import Messages
from django.forms import ModelForm


class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)