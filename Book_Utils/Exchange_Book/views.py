from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def list(request):
    return render(request, 'list.html')

def selling(request):
    return render(request, 'selling.html')


