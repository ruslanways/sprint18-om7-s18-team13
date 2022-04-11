from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        book = Book
        fields = ('namw', 'description', 'count', 'authors')