from django.shortcuts import render
from django.template import context

from goods.models import Products

def catalog(request): # запрос каталога

    # Получаем информацию из БД
    goods = Products.objects.all()

    context = {
        "title": "CustomPC Studio - Каталог",
        "goods": goods,
    }
    return render(request, 'goods/catalog.html', context)

def product(request): # запрос подробной информации о товаре
    context = {
        'title': 'CustomPC Studio - Продукт'
    }
    return render(request, 'goods/product.html', context)
