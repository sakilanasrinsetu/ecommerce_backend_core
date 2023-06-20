from utils.base import *

class ProductFilter(FilterSet):
    name = django_filters.CharFilter(label="name",
                                         method="filter_category")
    status = django_filters.BooleanFilter(label="status",
                                       method="filter_category")
    parent_product = django_filters.CharFilter(label="parent_product",
                                       method="filter_category")

    class Meta:
        model = Product
        fields = (
            "name",
            "status",
            "parent_product",
        )
    
    def filter_category(self, queryset, name, value):
        name = self.data.get('name')
        status = self.data.get('status')
        parent_product = self.data.get('parent_product')

        if name:
            queryset = queryset.filter(name__icontains = name)
            
        elif status:
            queryset = queryset.filter(status = status)

        elif parent_product:
            queryset = queryset.filter(
                parent_product__name__icontains = parent_product
                )

        return queryset
    