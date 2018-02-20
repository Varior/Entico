# -*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


# Модель категорії
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])


# Модель товару
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категорія")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Назва")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    top_image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Зображення товару")
    description = models.TextField(blank=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    stock = models.PositiveIntegerField(verbose_name="Кількість")
    available = models.BooleanField(default=True, verbose_name="Доступний")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.category.slug, self.slug])


# Модель фотографій
class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='products', verbose_name="Товар")
    name = models.CharField(max_length=50, db_index=True, verbose_name="Назва фотографії")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Зображення товару")

           
    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
          return reverse('shop:ProductDetail', args=[self.id, self.slug])