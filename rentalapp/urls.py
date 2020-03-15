from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('description/', views.description, name='description'),
    path('books/', views.books, name='books'),
    path('books/result/', views.result, name='result'),
]