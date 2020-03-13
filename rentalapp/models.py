from django.db import models
from django.conf import settings

# # Create your models here.
class Client(models.Model):
    #We have name, surname and email inside in-built user (in django)
    # name = models.CharField(max_length=30)
    # surname = models.CharField(max_length=30)
    # email = models.CharField(max_length=60)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.username)

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    ordered = models.BooleanField()
    
    def __str__(self):
        return f'{self.Title} by {self.author}'

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.name}'

class Orders(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    operation_date = models.DateField()
    start_date = models.DateField()
    expected_end_date = models.DateField()
    expanded_end_date = models.DateField()
    end_date = models.DateField()

    #Posible status which could be achieved by each order
    reserved = models.BooleanField()
    canceled = models.BooleanField()
    rented = models.BooleanField()
    delayed = models.BooleanField()
    expanded = models.BooleanField()
    returned = models.BooleanField()

    #actual status of ordered item
    status = models.CharField(max_length=30)

    
    def __str__(self):
        return f'{self.Title} by {self.author}'

class CategoryFilter(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)