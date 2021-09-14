from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import PopularBooks, Category1, Category2, Category3, TopMembers, Contact


def index(request):
    popular_books = PopularBooks.objects.all()
    category_1 = Category1.objects.all()
    category_2 = Category2.objects.all()
    category_3 = Category3.objects.all()
    top_members = TopMembers.objects.all()

    return render(request, "index.html", {'popular_books' : popular_books, 'category_1' : category_1, 'category_2' : category_2, 'category_3' : category_3, 'top_members' : top_members})


def contact(request):

    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        msg = request.POST['msg']

        contact = Contact(email=email, name=name, msg=msg)
        contact.save()
        messages.success(request, 'Profile details updated.')


    return render(request, "contact.html")

    #___________When submitted the same email address______ 
    #___________it should show an error message____________

    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     name = request.POST.get('name')
    #     msg = request.POST.get('msg')

    #     if Contact.objects.filter(email = email).exists():
    #         messages.info(request, "Email already taken")
    #         return redirect("contact.html")
        
    #     else:
    #         contact = Contact(email=email, name=name, msg=msg)
    #         contact.save()
        
    #     return render(request, "contact.html")


def sorry(request):
    return render(request, "sorry.html")

