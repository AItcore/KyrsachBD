from django.urls import path
from django.urls.conf import include
from django.views.generic.base import TemplateView
from .views import Register
from . import views

urlpatterns = [

    path('register/', Register.as_view(), name='register'),
    path('page=<page>/search=<filter>/', views.index, name='home'),
    path('', views.index, name='home'),
    path('', include('django.contrib.auth.urls')),
    path(r'<choose>Page=<page>/', views.CatalogChoose, name='CatalogChoose'),
    path(r'product/<id_product>/', views.ProductInfo, name='ProductInfo'),
    path('<page>/', views.index, name='home'),
]
