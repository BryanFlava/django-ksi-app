from django.shortcuts import render
# from .models import Posr
from django.http import HttpResponse

def index(request):
    context = {
        'heading':"Form Manual"
    }
    if request.method == 'POST':
        print("SUDAH BOSS")
        context['username'] = request.POST['username']
        context['address'] = request.POST['address']
        
    else:
        print("GET BOSS")
    return render(request, 'index.html', context)

def articles(request, year):
    year = year
    str = year
    return HttpResponse(year)
