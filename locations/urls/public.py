from django.conf.urls import url
from django.urls import path, include

from locations.views import *
app_name = 'public'

urlpatterns = [ 
    path('division/', DivisionViewSet.as_view(
        {"get": "list"}),name="division"),
    path('division/<pk>/', DivisionViewSet.as_view(
        {"get": "retrieve"}),name="division"),
    path('district/', DistrictViewSet.as_view(
        {"get": "list"}),name="district"),
    path('district/<pk>/', DistrictViewSet.as_view(
        {"get": "retrieve"}),name="district"),
    path('district_list/<division_id>/', DistrictViewSet.as_view(
        {"get": "district_list"}),name="district_list"),
    path('area/<pk>/', AreaViewSet.as_view(
        {"get": "retrieve"}),name="area"),
    path('area_list/<district_id>/', AreaViewSet.as_view(
        {"get": "area_list"}),name="area_list"),
    path('store_list/<area_id>/', StoreLocationViewSet.as_view(
        {"get": "store_list"}),name="store_list"),
]
