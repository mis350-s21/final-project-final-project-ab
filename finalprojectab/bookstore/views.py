from django.shortcuts import redirect, render , get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Book, Review , Book_sell
from .forms import OrderForm, RequestForm , Contact_usForm , ReviewForm , Book_sellForm
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
        'book': books.id,
        'author': "Anonymous",
        })
    if f.is_valid():
        f.save()
        return redirect('/bookstore/all_books/', s=books.slug)
    c = {
        'slug_book' : books,
        'reviews': rs,
        'form': f,
    }
    
    return render(request , 'book_details.html' , c )

def contact_us(request):
    cu = Contact_usForm(request.POST or None)
    if cu.is_valid():
        cu.save()
        return redirect("greeting")
    data = {
        'form' : cu ,
    }
    return render(request , 'contact_us.html' , data) 

@login_required
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

def add_book(request):
    f = Book_sellForm(request.POST or None , initial={
        'username' : request.user
    })
    if f.is_valid():
        f.save()
        return redirect("thankyou_add")
    data = {
        'form' : f ,
    }
    
    return render(request , "add_book.html" , data)

def thankyou_add(request): 
    data={}
    return render(request , 'thankyou_add.html' , data)

def customers_books_list(request):
    books = Book_sell.objects.all().order_by('title')
    data = {
        'all_books_list' : books,
    }
    return render(request , 'customers_books_list.html' , data)
def customer_book_details(request , s):
    books = Book_sell.objects.get(slug = s)
    c = {'slug_book' : books}
    return render(request , 'customer_book_details.html' , c )
    
def edit_book(request , s):
    p = get_object_or_404(Book_sell ,slug=s )
    f = Book_sellForm(request.POST or None , instance=p )
    c = {
        "book" : p ,
        'form':f , 
    } 
    if f.is_valid():
        f.save()
        return redirect("/bookstore/customers_books/" , s=p.slug)

    return render(request , 'add_book.html' , c)


def delete_book(request, s):
    p = get_object_or_404(Book_sell ,slug=s)
    c = {
        'message': f"delete post {p.title}",
    }
    if "confirm" in request.GET:
        p.delete()
        return redirect('/bookstore/customers_books/')
    elif "cancel" in request.GET:
        return redirect('/bookstore/customers_books/')
    return render(request, 'confirm.html', c)

def about(request): 
    data={}
    return render(request , 'about.html' , data)