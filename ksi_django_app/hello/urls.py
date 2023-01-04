from django.urls import include, path, re_path
from django.urls import path

from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.recent, name='form'),
    path('recent/', views.recent, name='recent'),
      path('post/', views.recent, name='post'),
    # re_path(r'^articles/(?P<year>[0-9]{4})/$', views.articles, name='dinamis'),
    re_path(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete'),
    # re_path(r'^update/(?P<id>[0-9]+)/$', views.update, name= 'update'),

]