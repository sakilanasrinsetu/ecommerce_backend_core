from catalog.serializers import CategorySerializer
from catalog.models import ProductGroup, Category, ProductBrand, TaxCategory
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from utils.custom_viewset import CustomViewSet
from rest_framework.permissions import IsAuthenticated
from utils.response_wrapper import ResponseWrapper

class PublicCategoryViewSet(CustomViewSet):
    queryset = Category.objects.all().exclude(status = 'child')
    serializer_class = CategorySerializer
    lookup_field = "pk"
    

    def retrieve(self, request, *args, **kwargs):
        qs = Category.objects.all()

        if kwargs.get("pk"):
            pk = kwargs.get("pk")
            if not pk.isdigit():
                qs = qs.filter(slug__iexact = str(pk)).last()
            else:
                qs = qs.filter(pk = pk).last()
        
        else:
            slug = kwargs["slug"]

            if not slug.isdigit():
                qs = qs.filter(slug__iexact = slug).last()
            else:
                qs = qs.filter(pk = int(slug)).last()

        if qs:
            serializer = self.get_serializer(qs)
            return ResponseWrapper(data = serializer.data, msg="Success")
        
        else:
            return ResponseWrapper(error_msg="Not found", error_code=404, status=404)
