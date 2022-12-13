from django.shortcuts import render
# from .models import Posr
from django.http import HttpResponse

def index(request):
    return HttpResponse("Testing")

def articles(request, year):
    year = year
    str = year
    return HttpResponse(year)