from django.shortcuts import redirect, render
from authentication.forms import AddUser
from authentication.serializers import UserSerializer
from order.models import Order
from . models import *
from rest_framework.viewsets import ModelViewSet

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

