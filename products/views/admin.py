from utils.base import *

# Create your views here.

class ProductCore:
    def product_create(self, serializer, *args, **kwargs):
        product_qs = None
        name = serializer.validated_data.get("name")
        status = serializer.validated_data.get("status")
        parent_product = serializer.validated_data.get("parent_product")
        selling_tax_category = serializer.validated_data.get("selling_tax_category")
        buying_tax_category = serializer.validated_data.get("buying_tax_category")
        brand = serializer.validated_data.get("brand")
        pos_product_info = serializer.validated_data.get("pos_product_info")
        discount = serializer.validated_data.get("discount")
        categories= serializer.validated_data.get("categories")
        sub_categories= serializer.validated_data.get("sub_categories")

        qs = self.queryset.filter(name = serializer.validated_data.get("name")).last()
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
        category_list = []
        if categories:
            for category in categories:
                category_qs = Category.objects.filter(
                    id = category.id).exclude(status = 'child').last()

                if category_qs:
                    category_list.append(category_qs.id)
        
        sub_category_list = []
        if sub_categories:
            for sub_category in sub_categories:
                sub_category_qs = Category.objects.filter(
                    id = sub_category.id, status = 'child').last()

                if sub_category_qs:
                    sub_category_list.append(sub_category_qs.id)
        
            
            
        qs = serializer.save(
            categories= category_list,
            sub_categories= sub_category_list,
            )

        # For Child Product, Parent Product Status Update
        if qs.status == "child":
            if qs.parent_product.status == 'standalone' or qs.parent_product.status == 'child':
                qs.parent_product.status = "parent"
                qs.parent_product.save()

        # Save Logger for Tracking 
        request_method = self.request.method
        request_url = self.request.build_absolute_uri()
        request_data = self.request.data 
        response_data = serializer.data
        
        try:
            send_action(qs, request_method, request_url,
                        request_data, response_data)
        except:
            pass

        product_qs = qs

        return product_qs

class AdminProductViewSet(CustomViewSet, ProductCore):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    lookup_field = "slug"
    search_fields = ['name']
    filterset_class = ProductFilter
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = ProductListSerializer
        elif self.action == 'pos_product_create':
            self.serializer_class = POSProductCreateSerializer
        else:
            self.serializer_class = self.serializer_class

        return self.serializer_class

    # TODO: Normal Product Check
    # TODO: POS Product Check

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if not serializer.is_valid():
            return ResponseWrapper(
                error_msg=serializer.errors,
                error_code=400,
                status=400
                )
        
        if request.data.get('is_only_pos') and not request.data.get('pos_product_info'):
            return ResponseWrapper(
                error_code=406,
                error_msg='For POS Product Need Pos Product Info',
                status=406
                )
        
        qs = self.product_create(serializer)

        # serializer = self.serializer_class(qs)
        serializer = self.serializer_class(qs)
        return ResponseWrapper(data = serializer.data, status=200, msg="Success")

    def pos_product_create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if not serializer.is_valid():
            return ResponseWrapper(error_msg=serializer.errors,
                                   error_code=400,
                                   status=400
                                   )
        
        if request.data.get('is_only_pos') and not request.data.get('pos_product_info'):
            return ResponseWrapper(
                error_code=406,
                error_msg='For POS Product Need POS Product Info Information',
                status=406
                )
        
        pos_product_info = serializer.validated_data.pop("pos_product_info")

        if pos_product_info:
            maximum_retail_price = pos_product_info.get('maximum_retail_price')
            minimum_selling_price = pos_product_info.get('minimum_selling_price')
            barcode_url = pos_product_info.get('barcode_url')
            commission_enabled = pos_product_info.get('commission_enabled')
            gsheba_amount = pos_product_info.get('gsheba_amount')
            pos_product_code = pos_product_info.get('pos_product_code')
            barcode = pos_product_info.get('barcode')
            barcode_serial_number = pos_product_info.get('barcode_serial_number')
            restock_quantity = pos_product_info.get('restock_quantity')
            quantity_per_shop = pos_product_info.get('quantity_per_shop')

            pos_product_info_qs = POSProductInfo.objects.create(
                maximum_retail_price = maximum_retail_price,
                minimum_selling_price = minimum_selling_price,
                barcode_url = barcode_url, commission_enabled = commission_enabled,
                gsheba_amount = gsheba_amount,
                pos_product_code = pos_product_code,
                barcode = barcode,
                barcode_serial_number = barcode_serial_number,
                restock_quantity = restock_quantity,
                quantity_per_shop = quantity_per_shop
            )

        pos_product_info = request.data.pop("pos_product_info")

        serializer = serializer_class(data=request.data,partial=True)

        # Product Create Function Call

        product_qs = self.product_create(serializer)

        # POS Product Info Create and Assign in Product Module

        product_qs.pos_product_info_id = pos_product_info_qs.id
        product_qs.is_only_pos = True
        product_qs.save()

        serializer = ProductListSerializer(product_qs)
        
        return ResponseWrapper(data=serializer.data,status=200, msg="Success")