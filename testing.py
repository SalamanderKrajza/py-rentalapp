#This is file which should assure that i don't have to import libraries each time i am using shell

#Shell is called by: 
    # python manage.py shell
#This file is called (INSIDE SHELL) by: 
    # exec(open('D:\\000.Dysk uporządkowany\\01. Wiedza\\05. Kursy\\Python\\rental\\testing.py').read()) 

from django.utils import timezone
from rentalapp.models import User, Author, Book, CategoryFilter, Category, Order, Action

#Create some records
#Author(name='Jacek', surname='Piekara').save()


# title = models.CharField(max_length=30)
# author = models.ForeignKey(Author, on_delete=models.CASCADE)
# status = models.CharField(max_length=30)
# ordered = models.BooleanField()

# Book(title='Sługa Boży', author=Author.objects.get(name='Jacek', surname='Piekara')).save()

# Author.objects.all()[0].book_set.all()

# author_name_filter = ''
# author_surname_filter = ''
# title_filter = ''
# author_list = Author.objects.filter(
#     name__contains=author_name_filter, 
#     surname__contains=author_surname_filter
#     )
# book_list = []
# for author in author_list:
#     temp = author.book_set.filter(title__contains=title_filter)
#     if temp.exists():
#         book_list.append(temp)



# class TwojaKlasa():
#     def __init__(self, name):
#         print(f'Twoja klasa jest tutaj, nazywa się {name}')
#         self.WypiszDupa()

#     def WypiszDupa(self):
#         print('dupa')

# class MojaKlasa(TwojaKlasa):
#     def __init__(self):
#         print('a to jest moje klasa')
#         super().__init__('papuga')

#     def mojametoda(self):
#         print('hehe')

# #twoja = TwojaKlasa()
# moja = MojaKlasa()
# MojaKlasa().mojametoda()


# def testfunc(arg1, *args, **kwargs):
#     print(f'Arg1 = {arg1}\n\n')
#     for arg in args:
#         print(f'{arg}')
    
#     print('\n\n')

#     for key, value in kwargs.items():
#         print(f'Key is: {key}, Value is: {value}')

class MojaKlasa():
    def __init__(self):
        self._test = 'test'

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, somevalue):
        self._test = somevalue


def bubblesort(mytab):
    temp = len(mytab)-1

    for x in range(temp):
        for y in range(temp-x):
            if mytab[y]>mytab[y+1]:
                mytab[y], mytab[y+1] = mytab[y+1], mytab[y]
    print(mytab)
