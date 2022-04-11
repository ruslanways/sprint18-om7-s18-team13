from django import forms
from .models import Book, Author


class AuthorsModelMultipleChoice(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj) -> str:
        return f"{obj.surname.title()} {obj.name.title()} {obj.patronymic.title()}"


class AddBook(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    authors = AuthorsModelMultipleChoice(queryset=Author.objects.all())
