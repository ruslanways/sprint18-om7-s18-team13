from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors, name='authors'),
    path('<int:author_id>/', views.authors, name='authors_int')
]
