from django.db import models

# В Django модель это синоним слова таблица

# Categories - имя класса; models.Model - наследуемся от класса Model который находится в пакете models
# Поле id во всех колассах которые описывает модель в django создается автоматически
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children', verbose_name='Идентификатор категории')

    # вложенный класс Meta
    # здесь мы можем назначить принудительно имя для таблицы т.к. по умолчанию имя таблицы это goods_categories (имя приложения_имя класса). Сделаем имя в единственном числе
    # verbose_name - альтернативное имя
    class Meta:
        # указываем как таблица будет отображаться в БД
        db_table = 'category'
        # указываем как таблица будет отображаться в админ панели
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    # Перегружаем метод __str__ для того чтобы в админ панели записи таблиц имели другие названия. Это можно сделать т.к. мы наследуемся от метода Model
    def __str__(self):
        return self.name


class Products(models.Model):

    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    # max_digits - знаки до запятой, decimal_digits - знаки после запятой
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    # Скидка в %. окончательнаю стоимость будет высчитываться
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    # quantity = stock = в наличие
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    # on_delete=models.PROTECT - при попытке удалить категорию к которой привязан как минимум 1 товар будет запрет на удаление
    # on_delete=models.CASCADE - при попытке удалить категорию к которой привязан как минимум 1 товар, все связанные товары с удаленной категорией будут удаленыс
    # on_delete=models.SET_DEFAULT, default= - при попытке удалить категорию к которой привязан как минимум 1 товар, всем связанным товарам будет присвоено значение категории по умолчанию которое мы и указываем тут
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'