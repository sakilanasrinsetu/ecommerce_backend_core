from django.urls import path
from blogs.views.public import (
    PublicBlogViewSet
)

app_name = 'public'


urlpatterns = [
    # path('blogs/', PublicBlogViewSet.as_view(
    #     {"get": "list"}),
    #                   name="blogs")
]
