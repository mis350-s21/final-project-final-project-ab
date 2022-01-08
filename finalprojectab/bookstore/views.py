from django.shortcuts import redirect, render

from .models import Book

from .forms import ReviewForm
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
    rs = books.review_set.all()
    f = ReviewForm(request.POST or None, initial={
        'books': books.id,
        'author': "Anonymous",
        })
    if f.is_valid():
        f.save()
        return redirect('book_details.html', s=books.slug)
    
    
    data = {
        'slug_book' : books,
        'review': rs,
        'form': f,
    }
    
    return render(request , 'book_details.html' , data)