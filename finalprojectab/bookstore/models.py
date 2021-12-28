from django.db import models

# Create your models here.

class Book(models.Model): 

    CART = (
        (0,"Not in Cart"),
        (1,"In Cart"),
    )

    category = models.CharField(max_length=50 , null=False)
    name = models.CharField(max_length=200, null=False , unique=True)
    slug = models.SlugField(max_length=200,unique=True  )
    image = models.ImageField()
    description = models.TextField(blank=True,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    Cart = models.IntegerField(choices=CART, default=0)

# this is a test
# part 2

