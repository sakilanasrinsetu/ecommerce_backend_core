import django_filters
from django_filters.rest_framework import FilterSet

from django.db.models import Count, Min, Q, query_utils
from locations.models import District, Area, StoreLocation

class DistrictFilter(FilterSet):
    division_id = django_filters.CharFilter(label="division_id",
                                           method="filter_district")

    class Meta:
        model = District
        fields = (
            "division_id",
        )

    def filter_district(self, objects, name, value):
        division_id = self.data.get('division_id')

        if division_id:
            queryset = District.objects.filter(
                division_id = division_id
            )

            return queryset

        else:
            queryset = District.objects.all()

            return queryset
        

class AreaFilter(FilterSet):
    district_id = django_filters.CharFilter(label="district_id",
                                           method="filter_area")

    class Meta:
        model = Area
        fields = (
            "district_id",
        )

    def filter_area(self, objects, name, value):
        district_id = self.data.get('district_id')

        if district_id:
            queryset = Area.objects.filter(
                district_id = district_id
            )

            return queryset

        else:
            queryset = Area.objects.all()
            
            return queryset

        

class StoreLocationFilter(FilterSet):
    area_id = django_filters.CharFilter(label="area_id",
                                           method="filter_store_location")

    class Meta:
        model = StoreLocation
        fields = (
            "area_id",
        )

    def filter_store_location(self, objects, name, value):
        area_id = self.data.get('area_id')

        if area_id:
            queryset = StoreLocation.objects.filter(
                area_id = area_id
            )

            return queryset

        else:
            queryset = StoreLocation.objects.all()
            
            return queryset
