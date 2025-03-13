from django.db import models
from django.db.models import CharField


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name',]



class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    image = models.ImageField( verbose_name='изображение',null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.BigIntegerField(verbose_name='цена')
    created_at = models.DateField(verbose_name='дата создания')
    updated_at = models.DateField(verbose_name='дата последнего изменения',null=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name',]





