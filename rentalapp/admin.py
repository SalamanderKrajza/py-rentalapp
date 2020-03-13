from django.contrib import admin

# Register your models here.
from .models import Client, Author, Book, Category, CategoryFilter

admin.site.register(Client)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(CategoryFilter)