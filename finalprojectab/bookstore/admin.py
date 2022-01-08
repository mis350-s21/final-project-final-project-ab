from django.contrib import admin
from .models import Book , Author , Customer, Review

# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review

class AuthorInLine(admin.TabularInline):
    model = Author

class BookAdmin(admin.ModelAdmin):
    list_display= ("name" , "price" , "available")
    inlines = [AuthorInLine , ReviewInline]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_name" , "customer_email" , "customer_num" , "customer_address")



admin.site.register(Book , BookAdmin)
admin.site.register(Customer , CustomerAdmin)