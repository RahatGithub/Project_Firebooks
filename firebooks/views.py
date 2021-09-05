from django.shortcuts import render
from .models import PopularBooks, Category1, Category2, Category3, TopMembers


def index(request):
    
    popular_books = PopularBooks.objects.all()
    category_1 = Category1.objects.all()
    category_2 = Category2.objects.all()
    category_3 = Category3.objects.all()
    top_members = TopMembers.objects.all()

    return render(request, "index.html", {'popular_books' : popular_books, 'category_1' : category_1, 'category_2' : category_2, 'category_3' : category_3, 'top_members' : top_members})


def sorry(request):
    return render(request, "sorry.html")