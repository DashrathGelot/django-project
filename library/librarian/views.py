from django.shortcuts import render
from .forms import book

def b_data(request):
    form=book(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'bform.html',{'data':book})
