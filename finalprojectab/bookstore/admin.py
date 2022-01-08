from django.contrib import admin

from .models import Book , Author, Contact_us , Customer, Request

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

admin.site.register(Book , BookAdmin)
admin.site.register(Customer , CustomerAdmin)
admin.site.register(Request , RequestAdmin)
admin.site.register(Contact_us , Contact_usAdmin)