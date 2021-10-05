from . models import *
from django import forms

class Schoolforms(forms.ModelForm):
    class Meta:
        model=Register
        fields=['e_id','name','age','post','salary','date']