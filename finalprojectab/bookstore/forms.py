from django import forms 
from django.forms import ModelForm

from . import models


class ReviewForm(forms.Modelform):
    class Meta:
        model = models.Review
        fields = ['review', 'author', 'email', 'post',]
        widgets = {
            'post': forms.HiddenInput(),
        }