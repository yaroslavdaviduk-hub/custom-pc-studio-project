from django.contrib import admin

# Register your models here.

# Регистрируем таблицы чтобы они отображались в админ панели
from goods.models import Categories, Products

# Эти два метода регистрации не позволяют вносить изменения в отображаемое в админ панели
# admin.site.register(Categories)
# admin.site.register(Products)

# Ниже представлено как модели (таблицы) регистрируются по нормальному (так же для того чтобы name автоматичетски переводился в slug)
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # Здесь передаем поля в словаре которые будут заполняться автоматически
    prepopulated_fields = {
        'slug': ('name',)
    }

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }