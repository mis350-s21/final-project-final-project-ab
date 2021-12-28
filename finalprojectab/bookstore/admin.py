from django.contrib import admin

from .models import Book , Author , Customer

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display= ("price" , "name" , "slug")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_name" , "customer_email" , "customer_num" , "customer_address")



admin.site.register(Book , BookAdmin)
admin.site.register(Customer , CustomerAdmin)