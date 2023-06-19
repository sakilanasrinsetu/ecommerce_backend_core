from django.urls import path
from products.views.admin import *

app_name = 'admin'

urlpatterns = [
    path('product/', AdminProductViewSet.as_view(
        {"get": "list", 'post':'create'}),
                      name="product"),
    path('product/<pk>/', AdminProductViewSet.as_view(
        {"patch": "update", 'delete':'destroy', 'get':'retrieve'}),
                      name="product"),
]