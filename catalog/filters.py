import django_filters
from django_filters.rest_framework import FilterSet

from django.db.models import Count, Min, Q, query_utils

from catalog.models import ProductGroup, Category, TaxCategory, ProductBrand


class ProductGroupFilter(FilterSet):
    is_featured = django_filters.CharFilter(label="is_featured",
                                         method="filter_product_group")
    is_active = django_filters.CharFilter(label="is_active",
                                       method="filter_product_group")
    slug = django_filters.CharFilter(label="slug",
                                        method="filter_product_group")
    show_in_ecommerce = django_filters.CharFilter(label="show_in_ecommerce",
                                       method="filter_product_group")

    class Meta:
        model = ProductGroup
        fields = (
            "is_featured",
            "is_active",
            "slug",
            "show_in_ecommerce",
        )

    def filter_product_group(self, queryset, name, value):
        is_featured = self.data.get('is_featured')
        is_active = self.data.get('is_active')
        slug = self.data.get('slug')
        show_in_ecommerce = self.data.get('show_in_ecommerce')

        q_objects = Q()


        if is_featured is not None:
            if is_featured.capitalize() == 'True':
                q_objects |= Q(is_featured=True)

        if is_active is not None:
            if is_active.capitalize() == 'True':
                q_objects |= Q(is_active=True)
        
        if slug:
            q_objects |= Q(slug__icontains=slug)


        if show_in_ecommerce is not None:
            if show_in_ecommerce.capitalize() == 'True':
                q_objects |= Q(show_in_ecommerce=True)

        if not slug:
            queryset = queryset.filter(Q(is_active = is_active) | Q(is_featured = is_featured) |Q(show_in_ecommerce = show_in_ecommerce))

        else:
            queryset = queryset.filter(Q(is_active = is_active) | Q(is_featured = is_featured) |Q(show_in_ecommerce = show_in_ecommerce)| Q(slug__icontains=slug))
        
        return queryset
    

class CategoryFilter(FilterSet):
    group__slug = django_filters.CharFilter(label="group__slug",
                                         method="filter_category")
    has_child = django_filters.BooleanFilter(label="has_child",
                                       method="filter_category")
    is_active = django_filters.BooleanFilter(label="is_active",
                                       method="filter_category")
    is_featured = django_filters.CharFilter(label="is_featured",
                                        method="filter_category")
    show_in_ecommerce = django_filters.CharFilter(label="show_in_ecommerce",
                                       method="filter_category")
    status = django_filters.CharFilter(label="status",
                                       method="filter_category")

    class Meta:
        model = Category
        fields = (
            "group__slug",
            "has_child",
            "is_featured",
            "is_active",
            "show_in_ecommerce",
            "status",
        )
    
    def filter_category(self, queryset, name, value):
        print('vvvvvvvvvvvvvvvvvvvvv')
        group__slug = self.data.get('group__slug')
        has_child = self.data.get('has_child')
        is_featured = self.data.get('is_featured')
        is_active = self.data.get('is_active')
        show_in_ecommerce = self.data.get('show_in_ecommerce')
        status = self.data.get('status')
        
        #TODO:
        if status:
            queryset = queryset.filter(status = status)

        return queryset
    

class TaxCategoryFilter(FilterSet):
    value_in_percentage = django_filters.CharFilter(label="value_in_percentage",
                                         method="filter_tax_category")
    # is_active = django_filters.BooleanFilter(label="is_active",
    #                                    method="filter_tax_category")
    # type = django_filters.CharFilter(label="type",
    #                                     method="filter_tax_category")

    class Meta:
        model = TaxCategory
        fields = (
            "value_in_percentage",
            "is_active",
            "type",
        )
    
    def filter_tax_category(self, queryset, name, value):
        value_in_percentage = self.data.get('value_in_percentage')
        is_active = self.data.get('is_active')
        type = self.data.get('type')
        
        #TODO:
        # if group__slug

        return queryset