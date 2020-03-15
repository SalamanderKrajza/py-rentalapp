from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Book
from .forms import SearchBooksForm


def index(request):
    """
    View which displays main page
    """

    template = loader.get_template("rentalapp/index.html")
    context = {}
    return HttpResponse(template.render(context, request))



def description(request):
    """
    View which displays description page
    """

    template = loader.get_template("rentalapp/description.html")
    context = {}
    return HttpResponse(template.render(context, request))

def books(request):
    """
    View which allow to manage books
    """
    if request.method == 'POST':
        form = SearchBooksForm(request.POST)
        if form.is_valid():
            #Get some result
            return HttpResponseRedirect('/book/result/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchBooksForm()

    template = loader.get_template("rentalapp/books.html")


    context = {'form':form}
    return HttpResponse(template.render(context, request))


def result(request):
    """
    View which allow to see result of searching
    """
    if request.method == 'POST':
        form = SearchBooksForm(request.POST)
    else:
        form = SearchBooksForm()

    template = loader.get_template("rentalapp/result.html")

    book_list = Book.objects.filter(
        title__contains=request.POST.get("given_title",""),
        author__name__contains=request.POST.get("given_author_name",""),
        author__surname__contains=request.POST.get("given_author_surname","")
        ).order_by('author__surname', 'author__name', 'title')

    author_list = []
    for book in book_list:
        author_list.append(book.author)
    author_list = list(set(author_list))

    context = {'book_list':book_list, 'author_list':author_list, 'form':form}
    return HttpResponse(template.render(context, request))
