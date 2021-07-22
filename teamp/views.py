from django.shortcuts import render;
import json;
import logging;

from django.http import HttpResponse;
from django.shortcuts import render;

# Create your views here.


from myanalysis.first import tp


def home(request):
    return render(request, 'home.html');


def tp1(request):
    return render(request, 'tp1.html');

def TP1(request):
    data =tp().TP1()
    return HttpResponse(json.dumps(data), content_type='application/json');

def tp32(request):
    return render(request, 'tp32.html');

def TP32(request):
    ott = request.GET['ott']
    print(ott)
    data = tp().TP32(ott)
    print('데이터 전송 성공')
    return HttpResponse(json.dumps(data), content_type='application/json');

def tp322(request):
    return render(request, 'tp322.html');