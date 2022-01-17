from django.contrib import admin

from .models import Book , Author, Contact_us , Customer, Order, Request, Review , Book_sell

# Register your models here.

class AuthorInLine(admin.TabularInline):
    model = Author

class BookAdmin(admin.ModelAdmin):
    list_display= ("name" , "price" , "available")
    inlines = [AuthorInLine , ]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_name" , "customer_email" , "customer_num" , "customer_address")

class RequestAdmin(admin.ModelAdmin):
    list_display = ("customer_name" , "customer_email" , "customer_num" , "book_request")

class Contact_usAdmin(admin.ModelAdmin):
    list_display = ("name" , "email" , "phone_num" , "problem" , "created_on" , "preferred_time")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer_name" , "email" , "customer_num" , "address" , "payment" , "created_on")

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("review" , "book" , "email")

class Book_sellAdmin(admin.ModelAdmin):
    list_display = ("title" , "author" , "category" , "price" , "states" , "username")

admin.site.register(Book , BookAdmin)
admin.site.register(Customer , CustomerAdmin)
admin.site.register(Request , RequestAdmin)
admin.site.register(Contact_us , Contact_usAdmin)
admin.site.register(Order , OrderAdmin)
admin.site.register(Review , ReviewAdmin)
admin.site.register(Book_sell , Book_sellAdmin)
