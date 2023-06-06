from django.utils.decorators import method_decorator
from blogs.serializers import BlogSerializer
from blogs.models import Blog
# from user.permissions import HasRequiredPermissionForMethod
# from base.helpers.func import create_slug, my_random_string, entries_to_remove
# from base.helpers.decorators import exception_handler
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

# from user.permissions import IsStaff, IsSuperUser



class AdminBlogListCreateAPIView(ListCreateAPIView):
    # permission_classes = (IsAuthenticated, (IsStaff | IsSuperUser))
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    search_fields = ['$title']

    # @method_decorator(exception_handler)
    def create(self, request, *args, **kwargs):
        title = self.request.data['title']
        # request.data['slug'] = create_slug(title=title, random_str=my_random_string(6))
        request.data['created_by'] = self.request.user.id
        return super(AdminBlogListCreateAPIView, self).create(request, *args, **kwargs)



class AdminBlogRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated, (IsStaff | IsSuperUser))
    serializer_class = BlogSerializer
    queryset = Blog.objects.all().filter()
    lookup_field = 'slug'
    removeable_keys = ('slug',)
    http_method_names = ['get', 'patch','delete']

    # def update(self, request, *args, **kwargs):
    #     updated_request_data = entries_to_remove(self.request.data, self.removeable_keys)
    #     self.request.data.update(updated_request_data)
    #     request.data['updated_by'] = self.request.user.id
    #     return super(AdminBlogRetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)