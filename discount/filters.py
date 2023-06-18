import django_filters
from django_filters.rest_framework import FilterSet

from django.db.models import Count, Min, Q, query_utils

from discount.models import Discount
from django.utils import timezone
from datetime import date, datetime, timedelta



class DiscountFilter(FilterSet):
    name = django_filters.CharFilter(label="name",
                                         method="filter_discount")
    start_date = django_filters.DateFilter(label="start_date",
                                       method="filter_discount")
    end_date = django_filters.DateFilter(label="end_date",
                                        method="filter_discount")
    start_time = django_filters.TimeFilter(label="start_time",
                                        method="filter_discount")
    end_time = django_filters.TimeFilter(label="end_time",
                                        method="filter_discount")
    discount_type = django_filters.CharFilter(label="discount_type",
                                        method="filter_discount")
    is_active = django_filters.BooleanFilter(label="is_active",
                                        method="filter_discount")

    class Meta:
        model = Discount
        fields = (
            "name",
            "start_date",
            "end_date",
            "start_time",
            "end_time",
            "discount_type",
            "is_active",
        )

    def filter_discount(self, queryset, name, value):
        name = self.data.get('name')
        start_date = self.data.get('start_date')
        end_date = self.data.get('end_date')
        start_time = self.data.get('start_time')
        end_time = self.data.get('end_time')
        discount_type = self.data.get('discount_type')
        discount_schedule_type = self.data.get('discount_schedule_type')
        is_active = self.data.get('is_active')

        if name:
            queryset = queryset.filter(name__icontains = name)
            return queryset
        
        elif discount_type:
            queryset = queryset.filter(discount_type = discount_type)
            return queryset
        
        elif discount_schedule_type:
            queryset = queryset.filter(discount_schedule_type = discount_schedule_type)
            return queryset
        
        elif start_date and end_date:
            queryset = queryset.filter(start_date__lte = start_date , end_date__gte = end_date)
            return queryset
        
        elif start_time and end_time:
            queryset = queryset.filter(start_time__lte = start_time , end_time__gte = end_time)
            return queryset
        
        elif is_active:
            queryset = queryset.filter(
                is_active = is_active.capitalize()
                )
        
        else:
            return queryset