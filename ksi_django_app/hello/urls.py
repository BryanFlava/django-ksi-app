from django.urls import path

from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.recent, name='form'),
    path('recent/', views.recent, name='recent'),
    path('post/', views.recent, name='post')

]