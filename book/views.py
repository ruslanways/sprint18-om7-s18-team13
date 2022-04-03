from django.shortcuts import render
from . models import *

def books(request, book_id=None):
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
    return render(request, 'book/books.html', param_with_book_id) if book_id else \
    render(request, 'book/books.html', param)