from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'myVD02/index.html')

def new(request):
    return render(request, 'myVD02/new.html')

def test(request):
    return HttpResponse('Это страница test!')
# Create your views here.