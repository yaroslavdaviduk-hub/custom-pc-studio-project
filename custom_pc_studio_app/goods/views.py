from django.shortcuts import render
from django.template import context

def catalog(request): # запрос каталога
    context = {
        'title': 'CustomPC Studio - Каталог'
    }
    return render(request, 'goods/catalog.html', context)

def product(request): # запрос подробной информации о товаре
    context = {
        'title': 'CustomPC Studio - Продукт'
    }
    return render(request, 'goods/product.html', context)