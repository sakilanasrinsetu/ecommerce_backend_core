from django.urls import path
from catalog.views.admin import (
    AdminProductGroupViewSet,
    AdminCategoryViewSet,
    AdminProductBrandViewSet
)
from catalog.views.public import (
    PublicProductGroupViewSet,
    PublicCategoryViewSet
    )
app_name = 'public'


urlpatterns = [
    path('product_group_list/', PublicProductGroupViewSet.as_view(
        {'get':'list'}),
                      name="product_group_list"),
    path('product_groups/<pk>/', AdminProductGroupViewSet.as_view(
        {'get':'retrieve'}),
                      name="product_groups"),
    path('category/', AdminCategoryViewSet.as_view(
        {"get": "list"}),
                      name="public_category"),
    path('category/<slug>/', AdminCategoryViewSet.as_view(
        { 'get':'retrieve'}),
                      name="public_category"),
    path('brand/', AdminProductBrandViewSet.as_view(
        {"get": "list"}),
                      name="public_product_brand"),
    path('brand/<pk>/', AdminProductBrandViewSet.as_view(
        {'get':'retrieve'}),
                      name="public_product_brand"),
    path('group_by_categories/<slug>/', PublicProductGroupViewSet.as_view(
        {'get':'retrieve'}),
                      name="group_by_categories"),
    path('product_child_category/', PublicCategoryViewSet.as_view(
        {'get':'list'}),
                      name="product_child_category"),
]
