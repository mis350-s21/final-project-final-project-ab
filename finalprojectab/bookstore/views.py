from django.shortcuts import redirect, render

from .models import Book
from .forms import OrderForm, RequestForm , Contact_usForm 
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

def contact_us(request):
    cu = Contact_usForm(request.POST or None)
    if cu.is_valid():
        cu.save()
        return redirect("greeting")
    data = {
        'form' : cu ,
    }
    return render(request , 'contact_us.html' , data) 

def order(request):
    ord = OrderForm(request.POST or None)
    if ord.is_valid():
        ord.save()
        return redirect("thankyou")
    data = {
        'form' : ord ,
    }
    return render(request , 'order.html' , data)

def thankyou(request): 
    data={}
    return render(request , 'thankyou.html' , data)