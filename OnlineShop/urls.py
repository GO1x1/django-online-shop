
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', HomePage.as_view(), name='index'),
    path('cart', cart, name='cart'),

    # path('shop', main_page, name='shop'),
    path('shop', MainPage.as_view(), name='shop'),
    path('shop/<slug:sex_slug>', MainPageSex.as_view(), name='sex'),
    # path('shop/<slug:sex_slug>', MainPageSex.as_view(), name='shop_sex'),
    # path('shop/women', main_page_women, name='shop_women'),
    # path('shop/women', MainPageWomen.as_view(), name='shop_women'),

    path('shop/brand/<slug:category_brands_slug>', MainPageBrand.as_view(), name='shop_brand'),
    path('shop/section/<slug:category_model_slug>', MainPageModel.as_view(), name='shop_model'),
    path('shop/type/<slug:category_for_slug>', MainPageType.as_view(), name='shop_type'),

    path('brand', about, name='about'),
    path('contact', contact, name='contact'),
    path('product/<int:product_id>', shop_single, name='shop_single'),
    path('add_to_cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('add_to_cart_and_go_cart/<int:product_id>', add_to_cart_and_go_cart, name='add_to_cart_and_go_cart'),

    path('card/add', card_add, name='card_add'),
    path('card/delete', card_delete, name='card_delete'),
    path('cart/delete/<int:pr_pk>', delete_p_f_cart, name='delete_p_f_cart'),
    path('cart/delete/all', delete_p_f_cart_all, name='delete_p_f_cart_all'),
    path('order', order, name='order'),
    path('order/create', order_create, name='order_create'),
    path('qount_plus/<int:prod_pk>', qount_plus, name='qount_plus'),
    path('qount_min/<int:prod_pk>', qount_min, name='qount_min'),


    path('login', login_page, name='login'),
    path('register', register, name='register'),
    path('logout_user', logout_user, name='logout_user'),

    path('product/<int:product_id>/comments', comments, name='comments'),
    path('product/<int:product_id>/comments/add', comments_add, name='comments_add'),
    path('product/<int:product_id>/comments/delete', comment_del, name='comment_del'),
    path('product/<int:product_id>/comments/edit', comment_edit, name='comment_edit'),

]
