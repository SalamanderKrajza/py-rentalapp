#This is file which should assure that i don't have to import libraries each time i am using shell

#Shell is called by: 
    # python manage.py shell
#This file is called (INSIDE SHELL) by: 
    # exec(open('D:\\000.Dysk uporządkowany\\01. Wiedza\\05. Kursy\\Python\\rental\\testing.py').read()) 

from django.utils import timezone
from rentalapp.models import User, Author, Book, CategoryFilter, Category, Order

#Create some records
#Author(name='Jacek', surname='Piekara').save()


# title = models.CharField(max_length=30)
# author = models.ForeignKey(Author, on_delete=models.CASCADE)
# status = models.CharField(max_length=30)
# ordered = models.BooleanField()

# Book(title='Sługa Boży', author=Author.objects.get(name='Jacek', surname='Piekara')).save()

# Author.objects.all()[0].book_set.all()