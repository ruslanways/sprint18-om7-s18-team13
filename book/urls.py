from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('<int:book_id>/', views.books)
]
