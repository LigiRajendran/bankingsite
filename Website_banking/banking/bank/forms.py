from django import forms
from .models import Applicationform
class ApplicationForms(forms.ModelForm):
    class Meta:
        model=Applicationform
        fields=['name','email','phn','branch']