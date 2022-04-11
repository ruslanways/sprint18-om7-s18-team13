from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        author = Author
        fields = ('name', 'surname', 'patronimic')