from django.urls import path
from catalog.views.admin import (
    AdminProductGroupViewSet,
    AdminCategoryViewSet,
    AdminTaxCategoryViewSet,
    AdminProductBrandViewSet
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
    path('tax_category/', AdminTaxCategoryViewSet.as_view(
        {"get": "list", 'post':'create'}),
                      name="tax_category"),
    path('tax_category/<slug>/', AdminTaxCategoryViewSet.as_view(
        {"patch": "update", 'delete':'destroy', 'get':'retrieve'}),
                      name="tax_category"),
    path('product_brand/', AdminProductBrandViewSet.as_view(
        {"get": "list", 'post':'create'}),
                      name="product_brand"),
    path('product_brand/<pk>/', AdminProductBrandViewSet.as_view(
        {"patch": "update", 'delete':'destroy', 'get':'retrieve'}),
                      name="product_brand"),
]
