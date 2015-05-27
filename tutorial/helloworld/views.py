from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base.html')


def helloworld(request):
    return render(request, 'helloworld.html')


def introduce(request):
    return render(request, 'introduce.html')
