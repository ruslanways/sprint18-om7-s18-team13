from django.shortcuts import render, redirect
from .forms import AddAuthor
from .serializers import AuthorSerializer
from .models import *
from rest_framework import viewsets


def authors(request, author_id=None):
    if request.method == 'POST':
        form = AddAuthor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
        else:
            form = AddAuthor()
    else:
        form = AddAuthor()

    param_with_author_id = {
        'title': 'Books by specific author',
        'author_id': author_id,
        'authors_id': Author.get_by_id(author_id)
    }
    param = {
        'form': form,
        'title': 'Authors',
        'all_authors': Author.objects.all(),
    }
    return render(request, 'author/authors.html', param_with_author_id) if author_id else \
        render(request, 'author/authors.html', param)


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
