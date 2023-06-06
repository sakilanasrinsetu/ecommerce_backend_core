from blogs.serializers import BlogSerializer
from blogs.models import Blog
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from utils.custom_viewset import CustomViewSet
from rest_framework.permissions import IsAuthenticated
from utils.response_wrapper import ResponseWrapper


class PublicBlogViewSet(CustomViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk" or "slug"

    search_fields = ['title']

    def get_permissions(self):
        permission_classes = []
        if self.action in ["create", "update", "delete"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        qs = Blog.objects.filter(title = request.data.get("title")).last()
        if qs:
            return ResponseWrapper(
                error_msg="Blog is Already Found", error_code=406, status=406
            )
        request.data['created_by'] = request.user
        return super(PublicBlogViewSet, self).create(request, *args,
                                                     **kwargs)

