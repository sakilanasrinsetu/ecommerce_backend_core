from django.urls import path
from blogs.views.public import (
    PublicBlogViewSet
)

app_name = 'admin'

urlpatterns = [
    path('blogs/', PublicBlogViewSet.as_view(
        {"get": "list", 'post':'create'}),
                      name="blog"),
    path('blogs/<slug>/', PublicBlogViewSet.as_view(
        {"patch": "update", 'delete':'destroy', 'get':'retrieve'}),
                      name="blog"),
]
