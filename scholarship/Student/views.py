from django.shortcuts import render
from django.http import HttpResponse
from .forms import register,apply
from .models import s_app

def S_Register(request):
    form=register(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'register.html',{'key':form})

def S_apply(request):
    form=apply(request.POST)
    # form1=s_app.objects.filter(Enrollment_No=160220107001)
    # form1=s_app.objects.all().filter(BirthDate__year='1998')
    # form1=s_app.objects.filter(Enrollment_No__endswith=1)
    # form1=s_app.objects.order_by('-City')
    form1=s_app.objects.order_by('City')
    if form.is_valid():
        form.save()
    return render(request,'apply.html',{'k2':form,'data':form1})
