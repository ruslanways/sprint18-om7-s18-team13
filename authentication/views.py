from django.shortcuts import render
from order.models import Order
from . models import *

def users(request, user_id):
    param_with_user_id = {
        'title': 'Books of specific user',
        'user_id': user_id,
        'users_id': Order.objects.filter(user=user_id).values('book').distinct()  
    }
    return render(request, 'authentication/users.html', param_with_user_id)
