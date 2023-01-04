"""ksi_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path
from django.http import HttpResponse

from . import views

from hello.views import index

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls', namespace='hello')),
    path('about/', include('about.urls', namespace='about')),
        path('form/', views.form, name='form'),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.articles, name='dinamis'),
    re_path(r'^delete/(?P<year>[0-9]+)/$', views.delete, name='delete'),
    re_path(r'^update/(?P<year>[0-9]+)/$', views.update, name='update'),
    path('', index),
    ]