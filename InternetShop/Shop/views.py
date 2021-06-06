from .forms import CommentForm, RegisterUserForm, SearchForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import auth
from .models import *

# Create your views here.

def index(request, page=1, ft=' '):
    page = int(page)
    maxPage = int(len(Product.objects.all())/10)
    listPage = []
    if maxPage < 6:
        for i in range(maxPage+1):
            listPage.append(i+1)
    else:
        if page > 3 and page-3 < maxPage:
            listPage = [1,2,'...',page-2,page-1,page,page+1,page+2, '...', maxPage-1,maxPage]
        else:
            listPage = [1,2,3,'...',maxPage-1,maxPage]
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['searchLine']
            return redirect(f'page=1/search={search}')
    else:
        form = SearchForm()
    context = {
        'product_list': Product.objects.all().filter(name__icontains=ft)[(page-1)*10:(page-1)*10+10],
        'image_list' : Image.objects.all(),
        'prevPage' : page-1,
        'nextPage' : page+1,
        'maxPage' : maxPage,
        'listPage' : listPage,
        'form' : form,
        'ft' : ft,
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
            search = form.cleaned_data['searchLine']
            return redirect(f'page=1/search={search}')
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
    form = ''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['searchLine']
            return redirect(f'page=1/search={search}')
    else:
        form = SearchForm()
    commentForm = ''
    user = auth.get_user(request)
    if user.is_authenticated:
        if request.method == 'POST':
            commentForm = CommentForm(request.POST)
            if commentForm.is_valid():
                comment = Feedback()
                comment.id_product = Product.objects.get(id=id_product)
                comment.id_user = auth.get_user(request)
                comment.text = commentForm.cleaned_data['comment']
                comment.rating = 5
                comment.save()
        else:
            commentForm = CommentForm()
    context = {
        'product' : Product.objects.get(id=id_product),
        'image_list' : Image.objects.filter(id_product=id_product),
        'feedback' : Feedback.objects.filter(id_product=id_product),
        'form' : form,
        'commentForm' : commentForm,
    }
    return render(request, 'Shop/Product.html', context=context)

class Register(CreateView):
    template_name = 'Shop/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form) :
        form.save()
        return HttpResponseRedirect(self.success_url)
