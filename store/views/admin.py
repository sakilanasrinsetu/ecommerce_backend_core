from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from store.serializers import StoreLiteSerializer, StorePaymentMethodSerializer, StoreSerializer, DistrictSerializer
from store.models import Store, District, StorePaymentMethod
from store.filters import StoreFilter, StorePaymentMethodFilter
from user.permissions import IsStaff, IsSuperUser, HasRequiredPermissionForMethod, IsReadOnly
from base.helpers.func import create_slug, entries_to_remove
from base.helpers.decorators import exception_handler


class AdminDistrictListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, (IsStaff | IsSuperUser),)
    serializer_class = DistrictSerializer
    queryset = District.objects.filter()
    filterset_fields = ['name']

class AdminStoreLiteListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, (IsStaff | IsSuperUser | IsReadOnly),)
    serializer_class = StoreLiteSerializer
    queryset = Store.objects.filter()
    filterset_fields = ['district']


class AdminStoreListCreateAPIView(ListCreateAPIView):
    # permission_classes = (IsSuperUser,)
    permission_classes = (HasRequiredPermissionForMethod,)
    get_permission_required = ['store.view_store', 'purchase.add_purchaseorderreturn', 'stock.add_stocktransfer','stock.add_stockadjustment', 'orders.view_order']
    post_permission_required = ['store.add_store']
    serializer_class = StoreSerializer
    queryset = Store.objects.select_related(
        'district', 'created_by', 'updated_by').filter()
    search_fields = ['name', 'district__name']
    filterset_class = StoreFilter

    @method_decorator(exception_handler)
    def create(self, request, *args, **kwargs):
        name = self.request.data['name']
        request.data['slug'] = create_slug(title=name)
        request.data['district'] = get_object_or_404(
            District, id=request.data['district']).id
        request.data['created_by'] = self.request.user.id
        # request.data['location'] = f"Point({self.request.data['lat']} {self.request.data['lon']})"
        return super(AdminStoreListCreateAPIView, self).create(request, *args, **kwargs)


class AdminStoreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (HasRequiredPermissionForMethod,)
    get_permission_required = ['store.view_store']
    patch_permission_required = ['store.change_store']
    delete_permission_required = ['store.delete_store']
    serializer_class = StoreSerializer
    queryset = Store.objects.select_related(
        'district', 'created_by', 'updated_by').filter()
    lookup_field = 'slug'
    http_method_names = ['get', 'patch','delete']
    removeable_keys = ('slug',)

    @method_decorator(exception_handler)
    def update(self, request, *args, **kwargs):
        updated_request_data = entries_to_remove(
            self.request.data, self.removeable_keys)
        self.request.data.update(updated_request_data)
        if request.data.get('district', None):
            district = get_object_or_404(
                District, id=request.data.get('district'))
            request.data['district'] = district.id
        if request.data.get('lat') and request.data.get('lon'):
            request.data['location'] = f"Point({self.request.data['lat']} {self.request.data['lon']})"
        request.data['updated_by'] = self.request.user.id
        return super(AdminStoreRetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)


class AdminStorePaymentMethodListLiteAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, IsStaff)
    serializer_class = StorePaymentMethodSerializer
    queryset = StorePaymentMethod.objects.select_related('store', 'created_by', 'updated_by').filter()
    search_fields = ['$name']
    filterset_class = StorePaymentMethodFilter

class AdminStorePaymentMethodListCreateAPIView(ListCreateAPIView):
    permission_classes = (HasRequiredPermissionForMethod,)
    post_permission_required = ['store.add_storepaymentmethod', 'orders.change_order',]
    get_permission_required = ['store.view_storepaymentmethod', 'orders.add_order', 'orders.view_order', 'orders.change_order']
    serializer_class = StorePaymentMethodSerializer
    queryset = StorePaymentMethod.objects.select_related(
        'store', 'created_by', 'updated_by').filter()
    search_fields = ['name']
    filterset_class = StorePaymentMethodFilter

    @method_decorator(exception_handler)
    def create(self, request, *args, **kwargs):
        store_slug = request.data['store']
        store = get_object_or_404(Store, slug=store_slug)
        request.data['store'] = store.id
        request.data['created_by'] = self.request.user.id
        return super(AdminStorePaymentMethodListCreateAPIView, self).create(request, *args, **kwargs)


class AdminStorePaymentMethodRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (HasRequiredPermissionForMethod,)
    patch_permission_required = ['store.change_storepaymentmethod']
    get_permission_required = ['store.view_storepaymentmethod']
    delete_permission_required = ['store.delete_storepaymentmethod']
    serializer_class = StorePaymentMethodSerializer
    queryset = StorePaymentMethod.objects.select_related(
        'store', 'created_by', 'updated_by').filter()
    http_method_names = ['patch','get', 'delete']

    @method_decorator(exception_handler)
    def patch(self, request, *args, **kwargs):
        if request.data.get('store'):
            store = get_object_or_404(Store, slug=request.data['store'])
            request.data['store'] = store.id
        request.data['updated_by'] = self.request.user.id
        return super(AdminStorePaymentMethodRetrieveUpdateDestroyAPIView, self).patch(request, *args, **kwargs)
