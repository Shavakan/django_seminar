from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base.html')


def helloworld(request):
    return render(request, 'helloworld.html', {'message': 'Hello, World!'})


def introduce(request):
    return render(request, 'introduce.html')


def me(request):
    ctx = {
        'name': 'ChangWon Lee',
        'nickname': 'Shavakan',
        'hobby': 'Wow',
        'age': 24,
        'relationship': 'single'
    }
    return render(request, 'me.html', ctx)
