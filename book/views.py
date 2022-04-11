from django.shortcuts import redirect, render
from book.forms import AddBook
from .serializers import BookSerializer
from .models import Book
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

def books(request, book_id=None, book_name=None):

    if request.method == 'POST':
        if book_id:
            if 'delete' in request.POST:
                Book.objects.get(id=book_id).delete()
                return redirect('books')
            form = AddBook(request.POST, instance=Book.objects.get(id=book_id))
        else:
            form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
        else:
            form = AddBook()

    param_with_book_id = {
        'title': 'Books by id',
        'book_id': book_id,
        'books_id': Book.get_by_id(book_id)
    }

    param = {
        'form': AddBook(),
        'title': 'Books',
        'all_books': Book.objects.all(),
        'all_books_sorted_asc': Book.objects.all().order_by('name', 'count'),
        'all_books_sorted_desc': Book.objects.all().order_by('-name', 'count')
    }

    if book_name:
        param_with_book_name = {
            'title': 'Books by book name',
            'book_name': book_name,
            'books_by_name': Book.objects.filter(name__contains=book_name)
         }
        return render(request, 'book/books.html', param_with_book_name)
    if book_id:
        param_with_book_id.update({'form': AddBook(instance=Book.objects.get(id=book_id))})
        return render(request, 'book/books.html', param_with_book_id)
    return render(request, 'book/books.html', param)


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer