from django.shortcuts import render, redirect

# Create your views here.
from .models import Book, Author, Order, Action
from .forms import SearchBooksForm
from django.utils import timezone


def index(request):
    """
    View which displays main page
    """
    context = {}
    return render(request, 'rentalapp/index.html', context)




def description(request):
    """
    View which displays description page
    """
    context = {}
    return render(request, 'rentalapp/description.html', context)

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

    context = {'form':form}
    return render(request, 'rentalapp/books.html', context)


def result(request):
    """
    View which allow to see result of searching
    """
    if request.method == 'POST':
        form = SearchBooksForm(request.POST)
    else:
        form = SearchBooksForm()

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
    return render(request, 'rentalapp/result.html', context)


def book_details(request, book_id):
    """
    View which displays description page
    """
    book = Book.objects.get(id=book_id)
    orders = Order.objects.filter(book=book).order_by('-date')
    
    context = {'book':book, 'orders':orders}
    return render(request, 'rentalapp/book_details.html', context)

def reserve_book(request, book_id):
    """
    View which displays description page
    """
    if request.method == 'POST':
        b = Book.objects.get(id=book_id)
        b.is_reserved = True
        b.save()
        o = Order(
            user=request.user, 
            book=b, 
            date=timezone.now(), 
            action_type = Action.objects.get(action='RESERVE')
            )
        o.save()
    return redirect('/')