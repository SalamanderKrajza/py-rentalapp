from django.contrib import admin

# Register your models here.
from .models import User, Author, Book, Category, CategoryFilter, Order

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(CategoryFilter)