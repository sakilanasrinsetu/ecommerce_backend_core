from utils.base import *

# Create your views here.



class AdminProductViewSet(CustomViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    search_fields = ['name']
    # filterset_class = ProductFilter
    permission_classes = (IsAuthenticated,)


    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if not serializer.is_valid():
            return ResponseWrapper(error_msg=serializer.errors, error_code=400, status=400)
        
        name = request.data.get("name")
        status = request.data.get("status")
        parent_product = request.data.get("parent_product")

        qs = self.queryset.filter(name = request.data.get("name")).last()
        if qs:
            return ResponseWrapper(
                error_msg="Product is Already Found", 
                error_code=406, status=406
            )
        return super(AdminProductViewSet, self).create(request, *args,
                                                     **kwargs)
             