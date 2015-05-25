from django.http import HttpResponse

# Create your views here.


def helloworld(request):
    return HttpResponse("Hello, World!")


def introduce(request):
    return HttpResponse("This is Shavakan, 24 years old, \
                        from Zul'jin, Azeroth.")
