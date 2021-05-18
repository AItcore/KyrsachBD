from .forms import RegisterUserForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request, page=0):
    page = int(page)
    context = {
        'product_list': Product.objects.all()[page*10:page*10+10],
        'image_list' : Image.objects.all(),
        'page' : page
    }
    return render(request, 'Shop/home.html', context=context)

def CatalogChoose(request, choose, page=0):
    page = int(page)
    context = {
        'product_list': Product.objects.filter(category=choose)[page*10:page*10+10],
        'image_list' : Image.objects.all(),
        'choose' : choose  
    }
    return render(request, 'Shop/Catalog.html', context=context)

def ProductInfo(request, id_product):
    context = {
        'product' : Product.objects.get(id=id_product),
        'image_list' : Image.objects.filter(id_product=id_product)
    }
    return render(request, 'Shop/Product.html', context=context)

class Register(CreateView):
    template_name = 'Shop/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form) :
        form.save()
        return HttpResponseRedirect(self.success_url)

class Login(CreateView):
    template_name = 'registration/login.html'
    # form_class = 
