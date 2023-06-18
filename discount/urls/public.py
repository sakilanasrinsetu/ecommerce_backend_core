from django.urls import path
from discount.views.public import (
    PublicDiscountViewSet
)

app_name = 'public'


urlpatterns = [
    path('discount_list/', PublicDiscountViewSet.as_view(
        {"get": "list"}),
                      name="discount_list"),
    path('discount_details/<pk>/', PublicDiscountViewSet.as_view(
        {"get": "retrieve"}),
        name="discount_details"),
]
