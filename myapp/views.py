from django.shortcuts import render
from django.http import HttpResponse
from .models import Kijakum

# Create your views here.
def index(req):
    return render(req, 'myapp/index.html')

def whatthefantastic(req):
    return HttpResponse('555')

def dosomething(req):
    return HttpResponse('I do nothing')

def myapp(req):
    kijakums = Kijakum.objects.all()
    return render(req, 'myapp/myapp.html', { 'kijakums': kijakums })

def kijdetail(req, id):
    #kij = Kijakum.objects.filter(title=title)
    kij = Kijakum.objects.get(id=id)
    return render(req, 'myapp/kijakum.html', { 'kij': kij})