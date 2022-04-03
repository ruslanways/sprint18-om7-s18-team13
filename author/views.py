from django.shortcuts import render
import author
from book.models import Book
from . models import *

def authors(request, author_id=None):
    param_with_author_id = {
        'title': 'Books for specific author',
        'author_id': author_id,
        'authors_id': Book.objects.filter(authors__pk=author_id)
    }
    param = {
        'title': 'Authors',
        'all_authors': Author.objects.all(),
    }
    return render(request, 'author/authors.html', param_with_author_id) if author_id else \
    render(request, 'author/authors.html', param)
