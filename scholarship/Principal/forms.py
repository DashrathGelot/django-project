from django import forms
from .models import t_register,t_data

class t_regi(forms.ModelForm):
    class Meta:
        model=t_register
        fields=['t_id','Name','Mo','Email']
class t_da(forms.ModelForm):
    class Meta:
        model=t_data
        fields=['d']