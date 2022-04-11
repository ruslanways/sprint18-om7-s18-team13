from django.shortcuts import render
from . models import *
# from django.db.models import F

def orders(request):
    all_orders = list(Order.objects.all().order_by('created_at','plated_end_at'))
    return render(request, 'order/orders.html', {'title': 'Library orders', 'all_orders': all_orders})


def breakers(request):
    breakers = [f"{breaker.user.last_name} {breaker.user.first_name} {breaker.user.middle_name}"
        for breaker in Order.get_not_returned_books()]
    return render(request, 'order/breakers.html', {'title': 'Library breakers', 'breakers': breakers})


def unordered(request):
    param = {
        'title': 'Unordered books',
        'unordered': Book.objects.all().exclude(id__in=Order.objects.all().values('book'))
    }

    return render(request, 'order/unordered.html', param)
