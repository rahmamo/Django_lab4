from django import forms
from .models import *

class Insertform(forms.Form):
    name = forms.CharField( max_length=20,label='User Name')
    nationalnumber = forms.CharField( max_length=12,label='nationalnumber')
    nationalnumber.widget.attrs['class'] = 'form-control form-control-user'
    name.widget.attrs['class'] = 'form-control form-control-user'


class Insertform2(forms.ModelForm):
    class Meta:
        model=Trainee
        fields = ["name","nationalnumber"]

