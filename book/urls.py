from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.BookView)

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:book_id>/', views.books, name='bookid'),
    path('<slug:book_name>/', views.books, name='slug')
]
