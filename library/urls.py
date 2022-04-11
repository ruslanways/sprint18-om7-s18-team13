"""djangoViewTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from posixpath import basename
from django.contrib import admin
from django.urls import include, path
from order.views import OrderView
from . import views
from authentication.views import UserOdersView, UserView
from rest_framework.routers import SimpleRouter
from author.views import AuthorView
from book.views import BookView

router = SimpleRouter()
router.register('users', UserView)
router.register('orders', OrderView)
router.register('authors', AuthorView)
router.register('books', BookView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/users/<int:pkuser>/orders/', UserOdersView.as_view({'get': 'list'}), name='user_order-list'),
    path('api/v1/users/<int:pkuser>/orders/<int:pk>/', UserOdersView.as_view({'get': 'retrieve'})),
    path('', views.index, name='main'),
    path('admin/', admin.site.urls),
    path('books/', include('book.urls')),
    path('orders/', include('order.urls')),
    path('authors/', include('author.urls')),
    path('users/', include('authentication.urls'))
]
