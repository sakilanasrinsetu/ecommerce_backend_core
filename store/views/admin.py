from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from store.models import Store, District, StorePaymentMethod
from utils.response_wrapper import ResponseWrapper
from utils.custom_viewset import CustomViewSet
from store.filters import StoreFilter, StorePaymentMethodFilter
from store.serializers import StoreSerializer, StorePaymentMethodSerializer
from locations.models import District


class AdminStoreViewset(CustomViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = "slug"
    permission_classes =  (IsAuthenticated,)

    filterset_class = StoreFilter

    def create(self, request, *args, **kwargs):
        if not request.data.get("name"):
            return ResponseWrapper(
                error_msg="Store Name is Required", 
                error_code=406, status=406
            )
        
        qs =self.queryset.filter(name = request.data.get("name")).last()
        if qs:
            return ResponseWrapper(
                error_msg="Store is Already Found", 
                error_code=406, status=406
            )    
        if not request.data.get("district"):
            return ResponseWrapper(
                error_msg="District is Required", 
                error_code=406, status=406
            )
        
        district_qs =District.objects.filter(
            id = request.data.get("district")).last()
        
        if not district_qs:
            return ResponseWrapper(
                error_msg="District is Not Found", 
                error_code=406, status=406
            )
        return super(AdminStoreViewset, self).create(request, *args,
                                                     **kwargs)


class AdminStorePaymentMethodViewset(CustomViewSet):
    queryset = StorePaymentMethod.objects.all()
    serializer_class = StorePaymentMethodSerializer
    lookup_field = "pk"
    permission_classes =  (IsAuthenticated,)

    filterset_class = StorePaymentMethodFilter

    def create(self, request, *args, **kwargs):
        if not request.data.get("name"):
            return ResponseWrapper(
                error_msg="Store Name is Required", 
                error_code=406, status=406
            )
          
        if not request.data.get("store"):
            return ResponseWrapper(
                error_msg="Store is Required", 
                error_code=406, status=406
            )
        
        store_qs =Store.objects.filter(
            id = request.data.get("store")).last()
        
        if not store_qs:
            return ResponseWrapper(
                error_msg="Store is Not Found", 
                error_code=406, status=406
            )
        
        qs = self.queryset.filter(name = request.data.get("name"), store_id = store_qs.id).last()
        if qs:
            return ResponseWrapper(
                error_msg=f"Store Payment Method is Already Found for '{store_qs.name}'", 
                error_code=406, status=406
            )  
        
        return super(AdminStorePaymentMethodViewset, self).create(request, *args,
                                                     **kwargs)
