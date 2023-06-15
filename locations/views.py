from django.shortcuts import render
from locations.models import *
from utils.custom_viewset import CustomViewSet
from utils.custom_pagination import CustomPagination
from utils.response_wrapper import ResponseWrapper
from locations.serializers import (DivisionSerializer, AreaSerializer,
                                    DistrictSerializer, StoreLocationSerializer)
from locations.filters import DistrictFilter, AreaFilter, StoreLocationFilter


# Create your views here.

class DivisionViewSet(CustomViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    lookup_field = "pk"


class DistrictViewSet(CustomViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    lookup_field = "pk"

    filterset_class = DistrictFilter

class AreaViewSet(CustomViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    lookup_field = "pk"

    filterset_class = AreaFilter

class StoreLocationViewSet(CustomViewSet):
    queryset = StoreLocation.objects.all()
    serializer_class = StoreLocationSerializer
    lookup_field = "pk"

    filterset_class = StoreLocationFilter