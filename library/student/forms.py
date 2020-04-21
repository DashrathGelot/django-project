from django import forms
from .models import Stinfo

class userdata(forms.ModelForm):
    class Meta:
        model=Stinfo
        fields=['name','enroll_n','birth_date']

    #for get method
    # name=forms.CharField(max_length=12)
    # enroll_n=forms.IntegerField()
    # email=forms.EmailField()
    # birth_date=forms.DateField()
    # Password=forms.PasswordInput()

    