from django.urls import path

from . import views

app_name = 'rentalapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('description/', views.description, name='description'),
    path('books/', views.books, name='books'),
    path('books/result/', views.result, name='result'),
    path('books/reserve/<str:book_id>/', views.reserve_book, name='reserve_book'),
    path('books/<str:book_id>/', views.book_details, name='book_details'),
]