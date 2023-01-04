from django.shortcuts import render
from hello.models import Posr
from django.http import HttpResponse
from urllib import request
from django import forms
from django.http import HttpResponseRedirect
from hello.models import Posr

def articles(request, year):
    year=year
    str=year
    return HttpResponse(year)


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

def recent(request):
        return HttpResponse("ini hello")

def delete(request, id):
    Posr.objects.filter(id=id).delete()
    return HttpResponseRedirect('/hello/')

def form(request):
    classform = forms.classform(request.POST or None)

    if request.method == 'POST':
        if classform.is_valid():
            classform.save()
            return HttpResponseRedirect('/hello/')

        context = {
            'heading':'Home',
            'classForm':classform
        }
        return render(request, 'form.html', context)

def update(request, id):
    updt = Posr.objects.get(id=id)
    data = {
        'title' : updt.title,
        'body'  : updt.body,
        'email' : updt.email,
    }
    classform = forms.classform(request.POST or None, initial=data, isinstance=updt)

    if request.method == 'POST':
        if classform.is_valid():
            classform.save()
            return HttpResponseRedirect('/hello/')

    context = {
        'heading':'updt',
        'classform':'classform'
    }
    return render(request, 'form.html', context)

def articles(request, year):
    year = year
    str = year
    return HttpResponse(year)
