from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
    path('sorry.html', views.sorry, name="sorry"),
    path('sci_fi.html', views.sci_fi, name="sci_fi"),
    path('literature.html', views.literature, name="literature"),
    path('history.html', views.history, name="history"),
]