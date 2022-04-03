from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors),
    path('<int:author_id>/', views.authors)
]
