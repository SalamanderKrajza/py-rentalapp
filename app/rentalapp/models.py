from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# # Create your models here.
# class User(models.Model):
#     #We have name, surname and email inside in-built user (in django)
#     # name = models.CharField(max_length=30)
#     # surname = models.CharField(max_length=30)
#     # email = models.CharField(max_length=60)
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     birth_date = models.DateField()
#     address = models.CharField(max_length=100)
#     is_librarian = models.BooleanField(default=False)

#     def __str__(self):
#         return str(self.user.username)

class Author(models.Model):
    name = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30, default='')
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} {self.secondname + " " if self.secondname!="" else ""}{self.surname}'


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_avaiable = models.BooleanField(default=True)
    is_reserved = models.BooleanField(default=False)
    
    def __str__(self):
        return f'"{self.title}" by {self.author}'


class Action(models.Model):
    action = models.CharField(max_length=60, default='CUSTOM')

    def __str__(self):
        return self.action

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField()
    end_date = models.DateField(null = True, blank=True)

    #We can: Reserve, Cancel-Reservation, Rent, Extend, Return
    action_type = models.ForeignKey(Action, on_delete=models.CASCADE)
    custom_action = models.CharField(max_length = 60, blank = True)

    def __str__(self):
        return f'{self.book} - {self.action_type}'

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.name}'

class CategoryFilter(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
