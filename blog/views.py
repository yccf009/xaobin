from django.shortcuts import render
from django.http import HttpResponse
from  blog.models import users


def home(request):
    return render(request,'blog/home.html')

def blog_name(request):
    myblog =users.objects.all()
    return render(request,'home.html',{'myblog':myblog})

def hello(request):
    return HttpResponse("HELLO WORLD")
def index(request):
    return render(request,'blog/index.html')
def sp(request):
    return render(request,'blog/sp.html')

