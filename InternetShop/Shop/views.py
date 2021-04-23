from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request, 'Shop/home.html')

def CatalogChoose(request, choose):
    context = {
        'choose': choose,
        'product_list': Product.objects.all(),
        'image_list' : Image.objects.all(),  
    }
    return render(request, 'Shop/Catalog.html', context=context)