from django.shortcuts import render
from django.http import request
from .forms import t_regi,t_da
from .models import t_register

def t_regis(request):
    form=t_regi(request.POST)
    form1=t_register.objects.all()
    if form.is_valid():
        form.save()
    return render(request,'tregister.html',{'k3':form,'k4':form1})

def t_data(request):
    form=t_da(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'data.html',{'k4':form})
