from django.db import models


# Create your models here.

class Book(models.Model): 

    CART = (
        (0,"Not in Cart"),
        (1,"In Cart"),
    )

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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


# this is a test
# part 2

