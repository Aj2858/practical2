from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return render(request, 'index.html')

def virat(request):
    return render(request, 'v.html')

def rohit(request):
    return HttpResponse('<marquee><h1>This is Rohit Sharma Page</h1></marquee>')