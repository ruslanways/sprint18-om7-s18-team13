from django import forms

from authentication.models import CustomUser
from book.models import Book
from .models import Order

class UsersModelChoice(forms.ModelChoiceField):
    def label_from_instance(self, obj) -> str:
        return f"{obj.last_name.title()} {obj.first_name.title()} {obj.middle_name.title()}"

class BooksModelChoice(forms.ModelChoiceField):
    def label_from_instance(self, obj) -> str:      
        return f"{obj.name.title()}"


class AddOrder(forms.ModelForm):

    plated_end_at = forms.DateTimeField(input_formats=["%d.%m.%Y", "%d.%m.%y"])

    class Meta:
        model = Order
        fields = 'user', 'book', 'plated_end_at'
    
    user = UsersModelChoice(queryset=CustomUser.objects.all())
    book = BooksModelChoice(queryset=Book.objects.all())
