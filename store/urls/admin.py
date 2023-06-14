from django.urls import path
from store.views.admin import (
    AdminStoreListCreateAPIView, AdminStoreRetrieveUpdateDestroyAPIView,
    AdminStorePaymentMethodListCreateAPIView, AdminStorePaymentMethodRetrieveUpdateDestroyAPIView,
    AdminDistrictListAPIView, AdminStoreLiteListAPIView, AdminStorePaymentMethodListLiteAPIView
)

app_name = 'admin'

urlpatterns = [
    path('district', AdminDistrictListAPIView.as_view(),
         name='admin-district-list'),
    path('store', AdminStoreListCreateAPIView.as_view(),
         name='admin-store-list-create'),
    path('store-lite', AdminStoreLiteListAPIView.as_view(),
         name='admin-store-list-lite'),
    path('store/<str:slug>', AdminStoreRetrieveUpdateDestroyAPIView.as_view(),
         name='admin-store-get-update-delete'),
    path('store-payment-method', AdminStorePaymentMethodListCreateAPIView.as_view(),
         name='admin-store-payment-method-list-create'),
    path('store-payment-method-lite', AdminStorePaymentMethodListLiteAPIView.as_view(),
         name='admin-store-payment-method-list-lite'),
    path('store-payment-method/<int:pk>', AdminStorePaymentMethodRetrieveUpdateDestroyAPIView.as_view(),
         name='admin-store-payment-method-update-delete'),
]
