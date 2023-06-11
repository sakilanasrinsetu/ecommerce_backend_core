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

    def list(self, request, *args, **kwargs):
        qs = self.queryset.exclude(status = 'child')
        serializer = self.serializer_class(qs, many= True)
        return ResponseWrapper(status=200, msg="Success", data=serializer.data)

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if not serializer.is_valid():
            return ResponseWrapper(error_msg=serializer.errors, error_code=400, status=400)

        name = request.data.get("name")
        status = request.data.get("status")
        category_parent = request.data.get( "category_parent")
        product_group = request.data.get( "product_group")

        # ....***.... Duplicate Category Check ....***....
        qs = Category.objects.filter(name = name).last()
        if qs:
            return ResponseWrapper(
                error_msg="Category is Already Found", 
                error_code=406, status=406
            )
        
        # ....***.... Product Group Check ....***....
        if not product_group:
            return ResponseWrapper(
                    error_msg="Parent Group is Required", 
                    error_code=404, status=404
                )
        
        product_group_qs = ProductGroup.objects.filter(id = product_group).last()
        if not product_group_qs:
            return ResponseWrapper(
                error_msg="Product Group is Not Found", 
                error_code=406, status=406
            )
        
        # ....***.... Parent Category Exist Check ....***....
        if status == 'child' and not category_parent:
            return ResponseWrapper(
                    error_msg="For Child Category Must be Needed Parent Category", 
                    error_code=404, status=404
                )
        
        if category_parent:
            category_qs = Category.objects.filter(id = category_parent).last()
            if not category_qs:
                return ResponseWrapper(
                    error_msg="Parent Category is Not Found", 
                    error_code=404, status=404
                )
        
            # ....***.... Stand Alone Category Parent Category Check ....***....
            if status=='standalone' and category_qs:
                return ResponseWrapper(
                    error_code=406, 
                    error_msg='This Category is a Stand Alone Category, So, No Need to Parent Category ID',
                    status=406
                )
        
            # ....***.... Parent Category Parent Category Check ....***....
            
            if status=='parent' and category_qs:
                return ResponseWrapper(
                    error_code=406, 
                    error_msg='This Category is a Parent Category, So, No Need to Parent Category ID',
                    status=406
                )
            
                # TODO: 

        qs = serializer.save(
            created_by=self.request.user
        )
        if qs.status == "child":
            a ='df'
            if qs.category_parent.status == 'standalone' or qs.category_parent.status == 'child':
                qs.category_parent.status = "parent"
                qs.category_parent.save()

        serializer = self.serializer_class(qs)
        return ResponseWrapper(data = serializer.data, status=200, msg="Success")

    def update(self, request, *args, **kwargs):
        if request.data.get("slug"):
            slug = request.data.pop("slug")

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, partial=True)

        if not serializer.is_valid():
            return ResponseWrapper(error_msg=serializer.errors,
                                    error_code=400, status=400)
        # ....***.... There is Checking lookup Field both for slug and pk or ID ....***....

        qs = Category.objects.filter(id = kwargs["pk"]).last()

        if not qs:
            return ResponseWrapper(
                error_msg="Category is Not Found", 
                error_code=406, status=406
            )

        # ....***.... Duplicate Category Check ....***....
        
        category_qs = Category.objects.filter(name = request.data.get("name")).exclude(id = qs.id).last()

        if category_qs:
            return ResponseWrapper(
                error_msg="Category Name is Already Found", 
                error_code=406, status=406
            )

        name = request.data.get("name") or qs.name
        status = request.data.get("status") or qs.status

        if request.data.get( "category_parent"):
            category_parent = request.data.get( "category_parent")
        elif qs.category_parent: 
            category_parent= qs.category_parent.id 
        else:
            category_parent = None

        product_group = request.data.get( "product_group") or qs.product_group.id
        
        if slug:
            slug = slug
        else:
            slug = qs.slug

        category_slug_qs = Category.objects.filter(slug = slug).exclude(id = qs.id).last()

        if category_slug_qs:
            return ResponseWrapper(
                error_msg="Category Slug is Already Found", 
                error_code=406, status=406
            )

        # ....***.... Product Group Check ....***....
        if not product_group:
            return ResponseWrapper(
                    error_msg="Parent Group is Required", 
                    error_code=404, status=404
                )
        
        product_group_qs = ProductGroup.objects.filter(id = product_group).last()
        if not product_group_qs:
            return ResponseWrapper(
                error_msg="Product Group is Not Found", 
                error_code=406, status=406
            )
        
        # ....***.... Parent Category Exist Check ....***....
        if status == 'child' and not category_parent:
            return ResponseWrapper(
                    error_msg="For Child Category Must be Needed Parent Category", 
                    error_code=404, status=404
                )
        
        if category_parent:
            category_qs = Category.objects.filter(id = category_parent).last()
            if not category_qs:
                return ResponseWrapper(
                    error_msg="Parent Category is Not Found", 
                    error_code=404, status=404
                )
        
            # ....***.... Stand Alone Category Parent Category Check ....***....
            if status=='standalone' and category_qs:
                return ResponseWrapper(
                    error_code=406, 
                    error_msg='This Category is a Stand Alone Category, So, No Need to Parent Category ID',
                    status=406
                )
        
            # ....***.... Parent Category Parent Category Check ....***....
            
            if status=='parent' and category_qs:
                return ResponseWrapper(
                    error_code=406, 
                    error_msg='This Category is a Parent Category, So, No Need to Parent Category ID',
                    status=406
                )
            
                # TODO: 

        qs = serializer.update(instance=qs, validated_data=serializer.validated_data)

        try:
            if qs:
                qs.updated_by_id = self.request.user.id
                qs.save()
        except:
            qs = qs
            
        if qs.status == "child":
            a ='df'
            if qs.category_parent.status == 'standalone' or qs.category_parent.status == 'child':
                qs.category_parent.status = "parent"
                qs.category_parent.save()

        serializer = self.serializer_class(qs)
        return ResponseWrapper(data = serializer.data, status=200, msg="Success")