from django.db import models


# Create your models here.

<<<<<<< HEAD
=======
class Book(models.Model): 

    CART = (
        (0,"Not in Cart"),
        (1,"In Cart"),
    )

    category = models.CharField(max_length=50 , null=False)
    name = models.CharField(max_length=200, null=False , unique=True)
    slug = models.SlugField(max_length=200,unique=True  )
    #image = models.ImageField()
    description = models.TextField(blank=True,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    Cart = models.IntegerField(choices=CART, default=0)

class Author(models.Model):
    Author_name = models.CharField(max_length=50 ,unique=True )

class Customer(models.Model):
    customer_name = models.CharField(max_length=50 , null=False)
    customer_email = models.EmailField()
    customer_num = models.IntegerField(null=False)
    customer_address = models.CharField(max_length= 100 , null=False)


# this is a test
# part 2

>>>>>>> Abdulaziz
