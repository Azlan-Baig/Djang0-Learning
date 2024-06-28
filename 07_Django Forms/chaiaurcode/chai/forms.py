from django import forms
from .models import chaiVariery

class ChaiVarieryForm(forms.Form):
    cha_varity = forms.ModelChoiceField(queryset=chaiVariery.objects.all(),label="Select chai variery")
    