"""
URL configuration for custom_pc_studio_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static

from custom_pc_studio_app import settings


urlpatterns = [
    path('admin/', admin.site.urls), # маршрут админ-панели
    path('', include('main.urls', namespace='main')), # в начале в кавычках указывается домен приложения (например blog/ если приложение связано с блогом, news/ если с новостями, catalog/ для каталога и т.д.) В нашем случае там ничего нет, так как это главная страница и страницы которые нельзя выделить в отдельное приложение (типа страницы о нас about/) С помощю пространства имен namespace мы указываем к какому именно приложению относятся эти адреса когда мы обращаемся к ним в шаблонах
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('user/', include('users.urls', namespace='user')),
    path('cart/', include('carts.urls', namespace='cart')),
]

# этот URL маршрут будет сюда подключен только в DEBUG режиме
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),

    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)