from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('breakers/', views.breakers, name='breakers'),
    path('unordered/', views.unordered, name='unordered')
]
