from django.urls import path

from . import views

urlpatterns = [
    path('', views.greeting , name="greeting"),
    path('all_books/', views.all_books_list),
    path('available_books/', views.available_books_list),
    path('unavailable_books/', views.unavailable_books_list),
    path('book/<str:s>/', views.books_list_Category),
    path('contact_us/' , views.contact_us),
    path('order/' , views.order , name= "order" ),
    path('thankyou/' , views.thankyou , name = "thankyou" ) , 
    path('add_book/' , views.add_book ) , 
    path('thankyou_add/' , views.thankyou_add , name = "thankyou_add" ) ,
    path('customers_books/', views.customers_books_list),
    path('customerbook/<str:s>' , views.customer_book_details),
    path('edit_book/<str:s>/' , views.edit_book , name = "edit_book"),
    path('delete_book/<str:s>/' , views.delete_book , name = "delete_book"),
    path('about/' , views.about , name = "about" ),
]