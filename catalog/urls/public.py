from django.urls import path
from catalog.views.admin import (
    AdminCategoryViewSet
)

app_name = 'public'


urlpatterns = [
    path('category/', AdminCategoryViewSet.as_view(
        {"get": "list"}),
                      name="public_category"),
    path('category/<slug>/', AdminCategoryViewSet.as_view(
        { 'get':'retrieve'}),
                      name="public_category"),
]
