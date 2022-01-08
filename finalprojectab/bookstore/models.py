from django.db import models
from django.db.models.fields import IntegerField
from django.forms.fields import EmailField


# Create your models here.

class Book(models.Model): 

    CART = (
        (0,"Not in Cart"),
        (1,"In Cart"),
    )


    Cart = models.IntegerField(choices=CART, default=0)
    category = models.CharField(max_length=50 , null=False)
    name = models.CharField(max_length=200, null=False , unique=True)
    slug = models.SlugField(max_length=200,unique=True  )
    #image = models.ImageField()
    description = models.TextField(blank=True,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    

class Author(models.Model):
    Author_name = models.CharField(max_length=50 ,unique=True )
    book = models.ForeignKey('Book' , on_delete=models.CASCADE)

class Customer(models.Model):
    customer_name = models.CharField(max_length=50 , null=False)
    customer_email = models.EmailField()
    customer_num = models.IntegerField(null=False)
    customer_address = models.CharField(max_length= 100 , null=False)

class Request(models.Model):
    customer_name = models.CharField(max_length=50 , null=False)
    customer_email = models.EmailField()
    customer_num = models.IntegerField(null=False)
    book_request = models.CharField(max_length=100 , null=False)

class Contact_us(models.Model):
    TIME = (
        (0 , "8 AM to 12PM"),
        (1 , "12 PM to 4 PM"), 
        (2 , "4 PM to 8 PM"),
    )
    name = models.CharField(max_length=50 , null=False)
    email = models.EmailField(null=False)
    phone_num = models.IntegerField(null=False)
    problem = models.TextField(null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    preferred_time =models.IntegerField(choices=TIME , default=0)

class Order(models.Model):
    METHOD = (
        (0 , "cash on delivery"),
        (1 , "online payment (you will receive it a text)")
    )
    customer_name = models.CharField(max_length=50 , null=False)
    email = models.EmailField(null=False)
    customer_num = models.IntegerField(null=False)
    address = models.CharField(max_length= 100 , null=False)
    payment = models.IntegerField(choices=METHOD , default= 0 )
    created_on = models.DateTimeField(auto_now_add=True)
# this is a test
# part 2

