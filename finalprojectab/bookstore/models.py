from django.db import models

# Create your models here.

class Book(models.Model): 

    CART = (
        (0,"Not in Cart"),
        (1,"In Cart"),
    )

<<<<<<< Updated upstream
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

=======
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Cart = models.IntegerField(choices=CART, default=0)

>>>>>>> Stashed changes
