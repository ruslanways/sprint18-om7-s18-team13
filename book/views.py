from django.shortcuts import render
from . models import *

def books(request, book_id=None, book_name=None):

    param_with_book_id = {
        'title': 'Books by id',
        'book_id': book_id,
        'books_id': Book.get_by_id(book_id)
    }

    param = {
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
        return render(request, 'book/books.html', param_with_book_id)
    return render(request, 'book/books.html', param)
