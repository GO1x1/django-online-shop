from django.contrib import admin

# Register your models here.
from OnlineShop.models import Product, Category_brands, Size, Sex, Category_model, Category_for, Color, Image, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Category_model)
class Category_modelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Category_for)
class Category_forAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Category_brands)
class Category_brandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(Order)
