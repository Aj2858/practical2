from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def manish(request):
    return render(request, 'r.html')

def dilip(request):
    return render(request, 'd.html')

def anj(request):
    return HttpResponse('<center><h1>Welcome to new World</h1></center>')
