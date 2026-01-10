from django.shortcuts import render
from django.template import context

def catalog(request): # запрос каталога
    context = {
        "title": "CustomPC Studio - Каталог",
        "goods": [
            {
                "image": "deps/images/goods/mg-1-silver-amd.webp",
                "name": "CPS1 | Silver",
                "graphics": "NVIDIA GeForce RTX 5060",
                "processor": "AMD Ryzen 5 9600X",
                "memory": "16GB RGB DDR5",
                "storadge": "1TB T-Force A440 Gen4 SSD",
                "price": 1499.00,
            },
            {
                "image": "deps/images/goods/mg-1-the-ascendant.webp",
                "name": "CPS1 | The Ascendant",
                "graphics": "NVIDIA GeForce RTX 5080",
                "processor": "AMD Ryzen 7 9800X3D",
                "memory": "32GB RGB DDR5 6400MT/s",
                "storadge": "2TB Gen4 SSD",
                "price": 2799.00,
            },
            {
                "image": "deps/images/goods/mg-1-the-titan.webp",
                "name": "CPS1 | The Titan",
                "graphics": "NVIDIA GeForce RTX 5090",
                "processor": "AMD Ryzen 7 9800X3D",
                "memory": "32GB RGB DDR5 6400MT/s",
                "storadge": "2TB Gen4 SSD",
                "price": 4799.00,
            },
            {
                "image": "deps/images/goods/mg-1-the-underdog.webp",
                "name": "CPS1 | The Underdog",
                "graphics": "NVIDIA GeForce RTX 5070",
                "processor": "AMD Ryzen 7 7800X3D",
                "memory": "32GB RGB DDR5 6400MT/s",
                "storadge": "2TB Gen4 SSD",
                "price": 1999.00,
            },
            {
                "image": "deps/images/goods/mg-1-the-wilding.webp",
                "name": "CPS1 | The Wilding",
                "graphics": "NVIDIA GeForce RTX 5060 Ti",
                "processor": "AMD Ryzen 5 9600X",
                "memory": "16GB RGB DDR5 6400MT/s",
                "storadge": "1TB Gen4 SSD",
                "price": 1699.00,
            },
        ],
    }
    return render(request, 'goods/catalog.html', context)

def product(request): # запрос подробной информации о товаре
    context = {
        'title': 'CustomPC Studio - Продукт'
    }
    return render(request, 'goods/product.html', context)
