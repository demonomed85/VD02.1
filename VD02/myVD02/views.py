from django.shortcuts import render


def index(request):
    return render(request, 'myVD02/index.html')

def new(request):
    return render(request, 'myVD02/new.html')

def page(request):
    return render(request, 'myVD02/page.html')

def page4(request):
    return render(request, 'myVD02/page4.html')
# Create your views here.