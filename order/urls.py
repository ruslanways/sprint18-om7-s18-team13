from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders),
    path('breakers/', views.breakers),
    path('unordered/', views.unordered)
]
