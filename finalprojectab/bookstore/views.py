from django.shortcuts import render

from .models import Book
# Create your views here.

def greeting(request):
    data={}
    return render(request , 'greeting.html' , context=data)

def all_books_list(request):
    books = Book.objects.all().order_by('name')
    data = {
        'all_books_list' : books,
    }
    return render(request , 'books_list.html' , data)

def available_books_list(request):
    books = Book.objects.filter(available = True ).order_by('name')
    data = {
        'all_books_list' : books,
    }
    return render(request , 'books_list.html' , data)

def unavailable_books_list(request):
    books = Book.objects.filter(available = False ).order_by('name')
    data = {
        'all_books_list' : books,
    }
    return render(request , 'books_list.html' , data)

def books_list_Category(request , s):
    books = Book.objects.get(slug = s)
    data = {
        'slug_book' : books,
    }
    
    return render(request , 'book_details.html' , data)