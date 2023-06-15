from django.urls import path
from blogs.views.admin import (
    AdminBlogViewSet
)

app_name = 'admin'

urlpatterns = [
    path('blogs/', AdminBlogViewSet.as_view(
        {"get": "list", 'post':'create'}),
                      name="blog"),
    path('blogs/<slug>/', AdminBlogViewSet.as_view(
        {"patch": "update", 'delete':'destroy', 'get':'retrieve'}),
                      name="blog"),
]
