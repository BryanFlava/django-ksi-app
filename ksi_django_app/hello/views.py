from django.shortcuts import render
from django import forms
from .models import Posr
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    db = Posr.objects.all()
    context = {
        'title':'Hello',
        'heading':'Hello',
        'subheading':'postingan',
        'post':db,
    }
    return render(request, 'hello/index.html', context)

def recent(request):
    return HttpResponse("Hello WORLD")

def delete(request, id):
    Posr.objects.filter(id=id).delete()
    return HttpResponseRedirect('/blog/')

def update(request, id):
    updt = Posr.objects.get(id=id)
    data = {
        'title' : updt.title,
        'body'  : updt.body,
        'email' : updt.email,
    }
    classform = forms.classform(request.POST or None, initial=data, instance=updt)

    if request.method =='POST':
        if classform.is_valid():
            classform.save()
            return HttpResponseRedirect('/hello/')

    context = {
        'heading':'Updt',
        'classform':classform
    }
    return render(request, 'form.html', context)