from django.http import HttpResponse
from django.shortcuts import render # функция render для отрисовки html страницы и отправки ее пользователю

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'CustomPC Studio - Главная',
        'categories': categories
    } # эти значения передаются с httpRequest
    
    return render(request, 'main/index.html', context) # request для отрисовки данных переданых с httpRequest; template_name - html-шаблон (.html) обычно все шаблоны хранятся в приложении к которому они относятся 

def about(request):
    context = {
        'title': 'CustomPC Studio - О нас',
        'text_on_page': 'Текст о том, почему наш магазин лучше всех других!!!'
    }
    return render(request, 'main/about.html', context)