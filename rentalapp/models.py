from django.db import models
from django.conf import settings

# # Create your models here.
class User(models.Model):
    #We have name, surname and email inside in-built user (in django)
    # name = models.CharField(max_length=30)
    # surname = models.CharField(max_length=30)
    # email = models.CharField(max_length=60)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    is_librarian = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

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

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    date = models.DateField()
    end_date = models.DateField()

    #We can: Reserve, Cancel-Reservation, Rent, Extend, Return
    action_type = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.book} - {action_type}'

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.name}'

class CategoryFilter(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)