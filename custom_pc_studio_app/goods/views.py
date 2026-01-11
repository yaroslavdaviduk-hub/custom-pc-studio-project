# контроллеры
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

def product(request, product_slug): # запрос подробной информации о товаре
    
    product = Products.objects.get(slug=product_slug)
    
    context = {
        'title': 'CustomPC Studio - Продукт',
        'product': product,
    }


    return render(request, 'goods/product.html', context=context)
