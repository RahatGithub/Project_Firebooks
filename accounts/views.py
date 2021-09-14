from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def register(request):
    
    if request.method == "POST" :

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        user = User.objects.create_user(username, email, password)

        user.save()

        return redirect("/")

    return render(request, "register.html")



def login(request):

    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user:

            auth.login(request, user)

            return redirect("/")

        else:
            
            return render(request, "login.html")


    return render(request, "login.html")


def logout(request):

    auth.logout(request)

    return redirect("/")

