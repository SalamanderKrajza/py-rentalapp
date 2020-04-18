from django.contrib import admin

# Register your models here.
from .models import Author, Book, Category, CategoryFilter, Order, Action

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_reserved', 'is_avaiable')
    list_filter = ('is_reserved', 'is_avaiable')
    search_fields = ('title', 'author__name', 'author__surname')

class OrderInline(admin.TabularInline):
    model = Order

class ActionAdmin(admin.ModelAdmin):
    list_display = ('action', 'count_actions')

    def count_actions(self, obj):
        return obj.
    inlines = [
        OrderInline,
    ]

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(CategoryFilter)
admin.site.register(Order)
admin.site.register(Action, ActionAdmin)



