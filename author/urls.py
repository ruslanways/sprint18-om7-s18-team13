from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.AuthorView)

urlpatterns = [
    path('', views.authors, name='authors'),
    path('<int:author_id>/', views.authors, name='authors_int')
]
