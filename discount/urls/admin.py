from django.urls import path
from discount.views.admin import (
    AdminDiscountViewSet
)

app_name = 'admin'

urlpatterns = [
    path('discount/', AdminDiscountViewSet.as_view(
        {"get": "list", 'post':'create'}),
                      name="discount"),
    path('discount/<pk>/', AdminDiscountViewSet.as_view(
        {"patch": "update", 'delete':'destroy', 'get':'retrieve'}),
                      name="discount"),
]
