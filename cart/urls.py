from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('clear', views.clear_all, name='clear_all'),
    path('quantity/plus/<int:product_id>/', views.cart_quantity_plus, name='cart_quantity_plus'),
    path('quantity/minus/<int:product_id>/', views.cart_quantity_min, name='cart_quantity_min'),
]
