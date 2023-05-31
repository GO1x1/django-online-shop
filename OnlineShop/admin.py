from django.contrib import admin

# Register your models here.
from OnlineShop.models import Product, Category_brands, Size, Sex, Category_model, Category_for, Color, Image, Card, \
    Cart, Order, Comment

admin.site.register(Product)
admin.site.register(Category_brands)
admin.site.register(Category_model)
admin.site.register(Category_for)
admin.site.register(Size)
admin.site.register(Sex)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(Card)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Comment)