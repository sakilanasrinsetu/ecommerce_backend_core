import django_filters
from django_filters.rest_framework import FilterSet

from django.db.models import Count, Min, Q, query_utils
from store.models import Store, StorePaymentMethod

class StoreFilter(FilterSet):
    created_at_after = django_filters.DateFilter(label="created_at_after",
                                           method="filter_store")
    created_at_before = django_filters.DateFilter(label="created_at_before",
                                           method="filter_store")
    created_by = django_filters.CharFilter(label="created_by",
                                           method="filter_store")
    district_name = django_filters.CharFilter(label="district_name",
                                           method="filter_store")
    district = django_filters.CharFilter(label="district",
                                           method="filter_store")
    is_active = django_filters.BooleanFilter(label="is_active",
                                           method="filter_store")
    phone = django_filters.BooleanFilter(label="phone",
                                           method="filter_store")
    search = django_filters.BooleanFilter(label="search",
                                           method="filter_store")

    class Meta:
        model = Store
        fields = (
            "created_at_after",
            "created_at_before",
            "created_by",
            "district_name",
            "district",
            "is_active",
            "phone",
            "search",
        )

    def filter_store(self, objects, name, value):
        created_at_after = self.data.get('created_at_after')
        created_at_before = self.data.get('created_at_before')
        created_by = self.data.get('created_by')
        district_name = self.data.get('district_name')
        district = self.data.get('district')
        is_active = self.data.get('is_active')
        phone = self.data.get('phone')
        search = self.data.get('search')
        
        queryset = objects.all()

        if created_at_after:
            queryset = queryset.filter(
                created_at__gte = created_at_after
            )

            return queryset
        
        elif created_at_before:
            queryset = queryset.filter(
                created_at__lte = created_at_before
            )

            return queryset
        
        elif created_by:
            queryset = queryset.filter(
                created_by = created_by
            )
            
            return queryset
        
        elif district:
            queryset = queryset.filter(
                district_id = int(district)
            )
            
            return queryset
        
        elif district_name:
            queryset = queryset.filter(
                district__name__icontains = district_name
            )
            
            return queryset
        
        elif is_active:
            queryset = queryset.filter(
                is_active = is_active.capitalize()
            )
            
            return queryset
        
        elif phone:
            queryset = queryset.filter(
                Q(primary_phone____icontains = phone) |
                Q(secondary_phone____icontains = phone) 
            )
            
            return queryset
        
        elif search:
            queryset = queryset.filter(
                  Q(name____icontains = search) 
                | Q(slug____icontains = search) 
                | Q(address____icontains = search) 
            )
            
            return queryset



        return queryset
        

class StorePaymentMethodFilter(FilterSet):
    store_slug = django_filters.CharFilter(label="store_slug",
                                           method="filter_store_payment_method")
    type = django_filters.CharFilter(label="type",
                                           method="filter_store_payment_method")
    search = django_filters.CharFilter(label="search",
                                           method="filter_store_payment_method")

    class Meta:
        model = StorePaymentMethod
        fields = (
            "store_slug",
            "type",
            "search",
        )

    def filter_store_payment_method(self, objects, name, value):
        store_slug = self.data.get('store_slug')
        type = self.data.get('type')
        search = self.data.get('search')

        queryset = objects.all()

        if store_slug:
            queryset = queryset.filter(
                store__slug = store_slug
            )

            return queryset

        elif type:
            queryset = queryset.filter(
                type = type
            )

            return queryset
        
        elif search:
            queryset = queryset.filter(
                Q(name__icontains = search)
                | Q(account_number = search)
            )

            return queryset

        return queryset
        
