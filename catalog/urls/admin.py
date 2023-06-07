from django.urls import path
from catalog.views.admin import (
    AdminProductGroupViewSet,
    AdminCategoryViewSet
)

app_name = 'admin'

urlpatterns = [
    path('product_groups/', AdminProductGroupViewSet.as_view(
        {"get": "list", 'post':'create'}),
                      name="product_groups"),
    path('product_groups/<pk>/', AdminProductGroupViewSet.as_view(
        {"patch": "update", 'delete':'destroy', 'get':'retrieve'}),
                      name="product_groups"),
    path('category/', AdminCategoryViewSet.as_view(
        {"get": "list", 'post':'create'}),
                      name="category"),
    path('category/<pk>/', AdminCategoryViewSet.as_view(
        {"patch": "update", 'delete':'destroy', 'get':'retrieve'}),
                      name="category"),
]
