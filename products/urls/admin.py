from django.urls import path
from products.views.admin import *

app_name = 'admin'

urlpatterns = [
    path('product/', AdminProductViewSet.as_view(
        {"get": "list", 'post':'create'}),
                      name="product"),
    path('product/<slug>/', AdminProductViewSet.as_view(
        {"patch": "update", 'delete':'destroy', 'get':'retrieve'}),
                      name="product"),
    path('pos_product/', AdminProductViewSet.as_view(
        {'post':'pos_product_create'}),
                      name="pos_product"),
]