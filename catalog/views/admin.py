from catalog.serializers import ProductGroupSerializer, CategorySerializer
from catalog.models import ProductGroup, Category
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from utils.custom_viewset import CustomViewSet
from rest_framework.permissions import IsAuthenticated
from utils.response_wrapper import ResponseWrapper
from catalog.filters import ProductGroupFilter, CategoryFilter


class AdminProductGroupViewSet(CustomViewSet):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer
    lookup_field = "pk"

    search_fields = ['name']
    filterset_class = ProductGroupFilter

    def get_permissions(self):
        permission_classes = []
        if self.action in ["create", "update", "delete"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        qs = ProductGroup.objects.filter(name = request.data.get("name")).last()
        if qs:
            return ResponseWrapper(
                error_msg="Product Group is Already Found", 
                error_code=406, status=406
            )
        return super(AdminProductGroupViewSet, self).create(request, *args,
                                                     **kwargs)
    
class AdminCategoryViewSet(CustomViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"

    search_fields = ['name']
    filterset_class = CategoryFilter

    def get_permissions(self):
        permission_classes = []
        if self.action in ["create", "update", "delete"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        qs = Category.objects.filter(name = request.data.get("name")).last()
        if qs:
            return ResponseWrapper(
                error_msg="Category is Already Found", 
                error_code=406, status=406
            )
        return super(AdminCategoryViewSet, self).create(request, *args,
                                                     **kwargs)