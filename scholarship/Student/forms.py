from .models import s_re,s_app
from django import forms

class register(forms.ModelForm):
    class Meta:
        model=s_re
        fields=['Enrollment_No','Name','BirthDate','Branch','Mobile_No','Email']

class apply(forms.ModelForm):
    class Meta:
        model=s_app
        fields=['Enrollment_No','Name','BirthDate','Branch','Mobile_No','Email','City','Annual_Income']
