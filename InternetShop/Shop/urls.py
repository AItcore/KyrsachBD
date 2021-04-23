from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path(r'catalog/<choose>/', views.CatalogChoose, name='CatalogChoose')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
