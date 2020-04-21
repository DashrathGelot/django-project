from django import forms
from .models import Book

class book(forms.ModelForm):
    class Meta:
        model=Book
        exclude=['name','isbn']

'''name=forms.CharField(max_length=50)
    isbn=forms.IntegerField()
    publish_date=forms.DateField()    
    ch=[
        ('n','Novel'),
        ('p','Programming'),
        ('l','Language')
    ]
    Category=forms.CharField(max_length=19,choices=ch)'''