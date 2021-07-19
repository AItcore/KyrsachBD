from django.contrib import admin

from django import forms

from .models import *

class ImageInline(admin.TabularInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


# Register your models here.
admin.site.register(Purchase)
admin.site.register(Product, ProductAdmin)
admin.site.register(Feedback)