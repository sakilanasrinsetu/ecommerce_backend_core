from utils.base import *

# Create your views here.


class AdminProductViewSet(CustomViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    search_fields = ['name']
    # filterset_class = ProductFilter
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = ProductListSerializer
        else:
            self.serializer_class = self.serializer_class

        return self.serializer_class


    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if not serializer.is_valid():
            return ResponseWrapper(error_msg=serializer.errors, error_code=400, status=400)
        
        name = request.data.get("name")
        status = request.data.get("status")
        parent_product = request.data.get("parent_product")
        selling_tax_category = request.data.get("selling_tax_category")
        buying_tax_category = request.data.get("buying_tax_category")
        brand = request.data.get("brand")
        pos_product_info = request.data.get("pos_product_info")
        discount = request.data.get("discount")
        category_list = request.data.get("categories")
        sub_category_list = request.data.get("sub_categories")
        discount = request.data.get("discount")

        qs = self.queryset.filter(name = request.data.get("name")).last()
        if qs:
            return ResponseWrapper(
                error_msg="Product is Already Found", 
                error_code=406, status=406
            )
        if status=='child' and not parent_product:
            return ResponseWrapper(
                    error_msg="For Child Product Must be Needed parent Product", 
                    error_code=404, status=404
                )
        if parent_product:
            parent_product_qs = Product.objects.filter(
                id = parent_product
            ).last()

            if not parent_product_qs:
                return ResponseWrapper(
                    error_msg="Parent Product is Not Found", 
                    error_code=404, status=404
                )
            
            # ....***.... Stand Alone Category Parent Category Check ....***....
            if status=='standalone' and parent_product_qs:
                return ResponseWrapper(
                    error_code=406, 
                    error_msg='This Product is a Stand Alone Product, So, No Need to Parent Product ID',
                    status=406
                )
            
            elif status =='parent' and parent_product_qs:
                return ResponseWrapper(
                    error_code=406, 
                    error_msg='This Product is a Parent Product, So, No Need to Parent Product ID',
                    status=406
                )
        
        if category_list:
            category_qs = Category.objects.filter(id__in = category_list).exclude(status = 'child')

            if not category_qs:
                return ResponseWrapper(
                    error_code=406, 
                    error_msg='Categories Not Found',
                    status=406
                )
        
        if sub_category_list:
            sub_category_qs = Category.objects.filter(id__in = sub_category_list, status = 'child')

            if not category_qs:
                return ResponseWrapper(
                    error_code=406, 
                    error_msg='Sub Category Not Found',
                    status=406
                )
            
            
        qs = serializer.save()

        # For Child Product, Parent Product Status Update
        if qs.status == "child":
            if qs.parent_product.status == 'standalone' or qs.parent_product.status == 'child':
                qs.parent_product.status = "parent"
                qs.parent_product.save()

        # Save Logger for Tracking 
        request_method = request.method
        request_url = request.build_absolute_uri()
        request_data = request.data 
        response_data = serializer.data
        
        try:
            send_action(qs, request_method, request_url,
                        request_data, response_data)
        except:
            pass
            
        
        # serializer = self.serializer_class(qs)
        serializer = self.serializer_class(qs)
        return ResponseWrapper(data = serializer.data, status=200, msg="Success")

             