from django.urls import path

from goods import views

app_name = 'goods' # нужно при указании пространства имен для маршрутов когда мы используем функцию namespace

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'), 
    path('search/', views.catalog, name='search'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]