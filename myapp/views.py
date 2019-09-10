from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req, 'myapp/index.html')

def whatthefantastic(req):
    return HttpResponse('555')

def dosomething(req):
    return HttpResponse('I do nothing')

def myapp(req):
    return render(req, 'myapp/myapp.html')