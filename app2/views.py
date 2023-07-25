from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def rohit(request):
    return render(request, 'r.html')

def Abhishek(request):
    return HttpResponse('<h1><center> Wlcome to Gujarat </center></h1>')

def rohan(request):
    return render(request, 'rohan.html')
