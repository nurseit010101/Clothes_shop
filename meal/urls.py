"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from .settings import MEDIA_ROOT, MEDIA_URL
from mealapp.views import *
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('catalog', catalog, name='catalog'),
    path('contackts', contackts, name='contackts'),
    path('message/', message, name='message'),
    path('signUp/', signUp, name='signUp'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('cart/', cart, name='cart'),
    path('addcart/<int:id>', addCart, name='addCart'),
    path('removeCart/<int:id>', removeCart, name='removeCart'),
    path('api/v1/clothes', ClothesAPIList.as_view()),
    path('api/v1/clothesList/<int:pk>', ClothesAPIUpdate.as_view()),
    path('api/v1/clothesDetaill/<int:pk>', ClothesAPIDelete.as_view()),
]

urlpatterns += static(MEDIA_URL,document_root = MEDIA_ROOT)
