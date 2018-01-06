from django.contrib import admin
from .models import Category, Product, ProductImages
# Модель категорії
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
# Модель товару
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'top_image', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image']
   

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages, ImagesAdmin)