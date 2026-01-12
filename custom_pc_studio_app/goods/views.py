# контроллеры
from unicodedata import category
from django.shortcuts import get_list_or_404, render 
from django.template import context

from goods.models import Products

def catalog(request, category_slug): # запрос каталога
    
    # Получаем информацию из БД
    if category_slug == 'komplektuyushie':
        goods = Products.objects.exclude(category=22)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        "title": "CustomPC Studio - Каталог",
        "goods": goods,
    }
    return render(request, 'goods/catalog.html', context)




def product(request, product_slug): # запрос подробной информации о товаре
    
    product = Products.objects.get(slug=product_slug)
    
    context = {
        'title': 'CustomPC Studio - Продукт',
        'product': product,
    }


    return render(request, 'goods/product.html', context=context)


