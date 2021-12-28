from django.contrib import admin

<<<<<<< HEAD
<<<<<<< Updated upstream
=======
from .models import Book
#bll
>>>>>>> Stashed changes
=======
from .models import Book

>>>>>>> Abdulaziz
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display= ("price" , "name" , "slug")



admin.site.register(Book , BookAdmin)