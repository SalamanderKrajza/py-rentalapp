from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Book, Author
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

    author_list = Author.objects.filter(
        name__contains=request.POST.get("given_author_name",""), 
        surname__contains=request.POST.get("given_author_surname","")
        )
    book_list = []
    for author in author_list:
        temp = author.book_set.filter(title__contains=request.POST.get("given_title",""))
        if temp.exists():
            book_list.append(temp)

    context = {'book_list':book_list, 'form':form}
    return HttpResponse(template.render(context, request))
