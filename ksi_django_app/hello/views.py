from django.shortcuts import render
from .models import Posr

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
