from .forms import RegisterUserForm, SearchForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request, page=1, filter='' ):
    page = int(page)
    maxPage = int(len(Product.objects.all())/10)
    listPage = {}
    if page > 3 and page-3 < maxPage:
        listPage = {1,2,'...',page-2,page-1,page,page+1,page+2, '...', maxPage-1,maxPage}
    else:
        listPage = {1,2,3,'...',maxPage-1,maxPage}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['filter']
            return HttpResponse(f'page=1/search={search}')
    else:
        form = SearchForm()
    context = {
        'product_list': Product.objects.all().filter(name__icontains=filter)[(page-1)*10:(page-1)*10+10],
        'image_list' : Image.objects.all(),
        'prevPage' : page-1,
        'nextPage' : page+1,
        'maxPage' : maxPage,
        'listPage' : listPage,
        'form' : form
    }
    return render(request, 'Shop/home.html', context=context)

def CatalogChoose(request, choose, page=1):
    page = int(page)
    maxPage = int(len(Product.objects.all())/10)
    listPage = {}
    if page > 3 and page-3 < maxPage:
        listPage = {1,2,'...',page-2,page-1,page,page+1,page+2, '...', maxPage-1,maxPage}
    else:
        listPage = {1,2,3,'...',maxPage-1,maxPage}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['filter']
            return HttpResponseRedirect(f'page=1/search={search}')
    else:
        form = SearchForm()
    context = {
        'product_list': Product.objects.filter(category=choose)[(page-1)*10:(page-1)*10+10],
        'image_list' : Image.objects.all(),
        'choose' : choose,
        'prevPage' : page-1,
        'nextPage' : page+1,
        'maxPage' : maxPage,
        'listPage' : listPage,
        'form' : form 
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

class searchForm(CreateView):
    def getSearchResult(request):
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                search = form.cleaned_data['search']
                return HttpResponseRedirect(search)
        else:
            form = SearchForm()
        return render(request, 'Shop/home.html', {'form': form})