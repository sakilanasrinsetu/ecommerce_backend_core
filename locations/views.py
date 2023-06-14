from django.shortcuts import render
from locations.models import *
from utils.custom_viewset import CustomViewSet
from utils.custom_pagination import CustomPagination
from utils.response_wrapper import ResponseWrapper
from locations.serializers import (DivisionSerializer, AreaSerializer,
                                    DistrictSerializer, StoreLocationSerializer)


# Create your views here.

class DivisionViewSet(CustomViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    lookup_field = "pk"


class DistrictViewSet(CustomViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    lookup_field = "pk"

    pagination_class = CustomPagination

    def district_list(self, request, division_id, *args, **kwargs):
        qs = self.queryset.filter(division_id = division_id)

        page_qs = self.paginate_queryset(qs)
        serializer = self.serializer_class(instance=page_qs, many=True)

        paginated_data = self.get_paginated_response(serializer.data)
        return ResponseWrapper(data=paginated_data.data, msg="Success", status=200)


class AreaViewSet(CustomViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    lookup_field = "pk"

    pagination_class = CustomPagination

    def area_list(self, request, district_id, *args, **kwargs):
        qs = self.queryset.filter(district_id = district_id)

        page_qs = self.paginate_queryset(qs)
        serializer = self.serializer_class(instance=page_qs, many=True)

        paginated_data = self.get_paginated_response(serializer.data)
        return ResponseWrapper(data=paginated_data.data, msg="Success", status=200)


class StoreLocationViewSet(CustomViewSet):
    queryset = StoreLocation.objects.all()
    serializer_class = StoreLocationSerializer
    lookup_field = "pk"

    pagination_class = CustomPagination

    def store_list(self, request, area_id, *args, **kwargs):
        qs = self.queryset.filter(area_id = area_id)

        page_qs = self.paginate_queryset(qs)
        serializer = self.serializer_class(instance=page_qs, many=True)

        paginated_data = self.get_paginated_response(serializer.data)
        return ResponseWrapper(data=paginated_data.data, msg="Success", status=200)
