from django.db import models

# Create your models here.
<<<<<<< Updated upstream
=======

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

# this is a test
>>>>>>> Stashed changes
