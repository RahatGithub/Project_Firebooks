from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sorry.html', views.sorry, name="sorry"),
]