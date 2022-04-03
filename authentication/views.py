from django.shortcuts import render
from order.models import Order
from . models import *

def users(request, user_id=None):

    param_with_user_id = {
        'title': 'Books of specific user',
        'user_id': user_id,
        'users_id': Order.objects.filter(user=user_id).only('book').distinct()
    }

    param = {
        'title': 'Users',
        'all_users': CustomUser.objects.all(),
    }

    return render(request, 'authentication/users.html', param_with_user_id) if user_id \
        else render(request, 'authentication/users.html', param)
