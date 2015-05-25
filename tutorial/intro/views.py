# -*- coding: utf-8 -*-
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('/intro/스팍스/(자기 학번)/(자기 이름)으로 가주세요!')


def me(request, city, town, name):
    s = u"나는 %s %s의 %s이다!" % (city, town, name)
    return HttpResponse(s)
