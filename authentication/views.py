from django.shortcuts import redirect, render
import pkg_resources
from authentication.forms import AddUser
from authentication.serializers import UserOrderSerializer, UserSerializer
from order.models import Order
from . models import *
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import generics


def users(request, user_id=None):

    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            form = AddUser()
    else:
        form = AddUser()

    param_with_user_id = {
        'title': 'Books of specific user',
        'user_id': user_id,
        'users_id': Order.objects.filter(user=user_id).only('book').distinct()
    }

    param = {
        'form': form,
        'title': 'Users',
        'all_users': CustomUser.objects.all(),
    }

    return render(request, 'authentication/users.html', param_with_user_id) if user_id \
        else render(request, 'authentication/users.html', param)


class UserView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserOdersView(ReadOnlyModelViewSet):

    serializer_class = UserOrderSerializer

    def get_queryset(self):
        pkuser = self.kwargs.get("pkuser")
        pk = self.kwargs.get("pk")
        if not pk:
            return Order.objects.filter(user_id=pkuser)
        return Order.objects.filter(pk=pk)
