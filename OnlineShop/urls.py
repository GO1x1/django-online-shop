
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('shop', MainPage.as_view(), name='shop'),
    path('shop/<slug:sex_slug>', MainPageSex.as_view(), name='sex'),
    path('shop/brand/<slug:category_brands_slug>', MainPageBrand.as_view(), name='shop_brand'),
    path('shop/section/<slug:category_model_slug>', MainPageModel.as_view(), name='shop_model'),
    path('shop/type/<slug:category_for_slug>', MainPageType.as_view(), name='shop_type'),

    path('brand', AboutPage.as_view(), name='about'),
    path('contact', HomePage.as_view(), name='contact'),

    path('product/<slug:product_slug>', ProductDetailView.as_view(), name='shop_single'),
    # path('order', order, name='order'),
    # path('order/create', order_create, name='order_create'),

    path('login', login_page, name='login'),
    path('register', register, name='register'),
    path('logout_user', logout_user, name='logout_user'),

]
