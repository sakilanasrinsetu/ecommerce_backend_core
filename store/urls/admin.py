from django.urls import path
from store.views.admin import (
    AdminStoreViewset,
    AdminStorePaymentMethodViewset
)

app_name = 'admin'

urlpatterns = [
     path('stores/', AdminStoreViewset.as_view(
        {"get": "list", 'post':'create'}),
                      name="store"),
     path('stores/<slug>/', AdminStoreViewset.as_view(
        {"patch": "update", 'delete':'destroy', 'get':'retrieve'}),
                      name="store"),
     path('store_payment_method/', AdminStorePaymentMethodViewset.as_view(
        {"get": "list", 'post':'create'}),
                      name="store_payment_method"),
     path('store_payment_method/<slug>/', AdminStorePaymentMethodViewset.as_view(
        {"patch": "update", 'delete':'destroy', 'get':'retrieve'}),
                      name="store_payment_method"),
]
