from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('<int:user_id>/', views.users, name='user_int')
]
