from django.shortcuts import render, HttpResponse
from .models import ToDo
from .models import BooksShop

def homepage(request):
    return render(request,"index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request,"test.html",{"todo_list":todo_list})

def books(request):
    books_list = BooksShop.objects.all()
    return render(request,"books.html",{"books_list": books_list})

def third(request):
    return HttpResponse("This is page test3")