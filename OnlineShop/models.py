from time import timezone

from django.db import models
from django.urls import reverse


class Category_brands(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('shop_brand', kwargs={'category_brands_slug': self.slug})

    def __str__(self):
        return f'{self.title}'


class Category_model(models.Model):
    title = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='photo', blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('shop_model', kwargs={'category_model_slug': self.slug})

    def __str__(self):
        return f'{self.title}'


class Category_for(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('shop_type', kwargs={'category_for_slug': self.slug})

    def __str__(self):
        return f'{self.title}'


class Size(models.Model):
    size = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.size}'


class Color(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.size}'


class Sex(models.Model):
    title = models.CharField(max_length=10)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('sex', kwargs={'sex_slug': self.slug})

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.IntegerField()
    in_stock = models.BooleanField
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='photo', blank=True)

    size = models.ManyToManyField(Size, blank=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, blank=True, null=True)
    color = models.ManyToManyField(Color, blank=True)

    category_brands = models.ForeignKey(Category_brands, on_delete=models.CASCADE, blank=True, null=True)
    category_model = models.ForeignKey(Category_model, on_delete=models.CASCADE, blank=True, null=True)
    category_for = models.ForeignKey(Category_for, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    rating = models.IntegerField()

    def get_absolute_url(self):
        return reverse('shop_single', kwargs={'product_slug': self.slug})

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return f'{self.product}'


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField(null=True)
    quantity_prod = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.user}, {self.product}, {self.date}, {self.cost}'

