from django import template
# from OnlineShop.models import
from OnlineShop.models import Category_for, Category_model, Product

register = template.Library()

@register.simple_tag()
def category_type():
    return Category_for.objects.all()

@register.simple_tag()
def categor_model():
    return Category_model.objects.all()[:3]

@register.simple_tag()
def featured_product():
    return Product.objects.order_by('-rating')[:3]