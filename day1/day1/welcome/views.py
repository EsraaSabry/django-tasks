from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greattingparam(request,name):
    context = {}
    context['name'] = name
    return render(request,'welcome/welcome.html',context)