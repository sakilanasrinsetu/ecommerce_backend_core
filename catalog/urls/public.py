from django.urls import path
from catalog.views.admin import (
    AdminCategoryViewSet
)
from catalog.views.public import(
    PublicCategoryViewSet
)

app_name = 'public'


urlpatterns = [
    path('category/', AdminCategoryViewSet.as_view(
        {"get": "list"}),
                      name="public_category"),
    path('category/<slug>/', PublicCategoryViewSet.as_view(
        { 'get':'retrieve'}),
                      name="public_category"),
]
