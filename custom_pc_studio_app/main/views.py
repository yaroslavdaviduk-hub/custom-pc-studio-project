from django.http import HttpResponse
from django.shortcuts import render # функция render для отрисовки html страницы и отправки ее пользователю

def index(request):
    context = {
        'title': 'Home',
        'content': 'Main page',
        'list': ['first', 'second'],
        'dict': {'first': 1}, 
        'is_authenticated': False
    } # эти значения передаются с httpRequest
    return render(request, 'main/index.html', context) # request для отрисовки данных переданых с httpRequest; template_name - html-шаблон (.html) обычно все шаблоны хранятся в приложении к которому они относятся 

def about(request):
    return HttpResponse('About page')