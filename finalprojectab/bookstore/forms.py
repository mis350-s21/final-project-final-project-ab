from django import forms
from django.forms import fields, widgets

from . import models

class RequestForm(forms.ModelForm):
    class Meta:
        model = models.Request
        fields = ['customer_name' , 'customer_email' , 'customer_num' , 'book_request']