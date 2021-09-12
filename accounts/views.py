from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def register(request):
    
    if request.method == "POST" :

        email = request.POST.get('email')

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = User.objects.create_user(username, email, password)

        user.save()

        return redirect("/")

    return render(request, "register.html")



def login(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            return redirect("/")

        else:
            
            return render(request, "login.html")


    return render(request, "login.html")


def logout(request):
    pass