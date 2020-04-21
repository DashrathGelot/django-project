from django.shortcuts import render
from django.http import HttpResponse
from .forms import userdata

# Create your views here.
def hello(request):
    return HttpResponse("ewjhg")
'''
def data(request):
    abc=userdata()
    return render(request,'form1.html',{'key':abc,})'''

def datam(request):
    form=userdata(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'form1.html',{'key':form})