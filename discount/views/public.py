from blogs.serializers import BlogSerializer
from blogs.models import Blog
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from utils.custom_viewset import CustomViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from utils.response_wrapper import ResponseWrapper


class PublicBlogViewSet(CustomViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk" or "slug"

    search_fields = ['title']
