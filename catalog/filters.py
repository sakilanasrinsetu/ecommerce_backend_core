import django_filters
from django_filters.rest_framework import FilterSet

from django.db.models import Count, Min, Q, query_utils

from catalog.models import ProductGroup, Category


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

    class Meta:
        model = Category
        fields = (
            "name",
        )