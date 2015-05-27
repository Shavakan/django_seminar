from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base.html')


def helloworld(request):
    return HttpResponse("Hello, World!")


def introduce(request):
    return HttpResponse("This is Shavakan, 24 years old, \
                        from Zul'jin, Azeroth.")
