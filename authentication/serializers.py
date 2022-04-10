from rest_framework.serializers import ModelSerializer

from order.models import Order
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserOrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
