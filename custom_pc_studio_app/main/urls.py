# для того чтобы не запутаться в url так как их может быть очень много в файле custom_pc_studio_app/urls.py мы создаем в каждом приложении свой собственный файл urls.py.
# в файле custom_pc_studio_app/urls.py не забываем подключить этот файл main/urls.py иначе работать не будет

from django.urls import path

from main import views

app_name = 'main' # нужно при указании пространства имен для маршрутов когда мы используем функцию namespace

urlpatterns = [
    path('', views.index, name='index'), # маршрут домашней (главной) страницы
    path('about/', views.about, name='about'),
]