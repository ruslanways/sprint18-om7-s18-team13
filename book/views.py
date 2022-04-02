from django.shortcuts import render
from . models import *

def books(request, book_id=None):
    return render(request, 'book/books.html', {'title': 'Books by id', 'book_id': book_id, 'books_id': Book.get_by_id(book_id)}) if book_id else \
    render(request, 'book/books.html', {'title': 'Books', 'all_books': Book.objects.all()})
