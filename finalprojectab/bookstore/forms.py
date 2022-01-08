from django import forms
from django.forms import fields, widgets

from . import models

class RequestForm(forms.ModelForm):
    class Meta:
        model = models.Request
        fields = ['customer_name' , 'customer_email' , 'customer_num' , 'book_request']

class Contact_usForm(forms.ModelForm):
    class Meta:
        model = models.Contact_us
        fields = ["name" , "email" , "phone_num" , "problem" , "preferred_time"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['review', 'author', 'email', 'post',]
        widgets = {
            'post': forms.HiddenInput(),
        }