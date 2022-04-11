from django.shortcuts import redirect, render
from order.forms import AddOrder
from order.serializers import OrderSerializer
from . models import *
from rest_framework.viewsets import ModelViewSet

def orders(request):

    if request.method == 'POST':
        form = AddOrder(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
        else:
            form = AddOrder()
    else:
        form = AddOrder()

    all_orders = Order.objects.all().order_by('created_at','plated_end_at')
    return render(request, 'order/orders.html', {'title': 'Library orders', 'all_orders': all_orders, 'form': form})


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


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer