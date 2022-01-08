from django.shortcuts import redirect, render

from .models import Book
from .forms import RequestForm , Contact_usForm
# Create your views here.

def greeting(request):
    data={}
    br = RequestForm(request.POST or None )
    if br.is_valid():
        br.save()
        return redirect("greeting")
    data = {'form' : br}
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

def contact_us(request):
    cu = Contact_usForm(request.POST or None)
    if cu.is_valid():
        cu.save()
        return redirect("greeting")
    data = {
        'form' : cu ,
    }
    return render(request , 'contact_us.html' , data)