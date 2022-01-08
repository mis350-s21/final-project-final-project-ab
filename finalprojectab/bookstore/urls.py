from django.urls import path

from . import views

urlpatterns = [
    path('', views.greeting , name="greeting"),
    path('all_books/', views.all_books_list),
    path('available_books/', views.available_books_list),
    path('unavailable_books/', views.unavailable_books_list),
    path('book/<str:s>/', views.books_list_Category),
    path('contact_us/' , views.contact_us),
]