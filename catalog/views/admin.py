from catalog.serializers import ProductGroupSerializer
from catalog.models import ProductGroup
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from utils.custom_viewset import CustomViewSet
from rest_framework.permissions import IsAuthenticated
from utils.response_wrapper import ResponseWrapper
from catalog.filters import ProductGroupFilter


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