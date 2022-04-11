from django import forms
from .models import CustomUser

class AddUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = 'email', 'password', 'first_name', 'middle_name', 'last_name'
