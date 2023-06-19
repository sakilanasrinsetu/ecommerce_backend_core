from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug',"status","discount" ,"parent_product","is_active","is_featured","show_in_ecommerce","ordering","created_at"]

    class Meta:
        model = Product
    exclude = ['slug',]

admin.site.register(Product, ProductAdmin)

class ProductSellerAdmin(admin.ModelAdmin):
    list_display = ['id',"seller"]

    class Meta:
        model = ProductSeller

admin.site.register(ProductSeller, ProductSellerAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['id',"product", "rating", "is_accepted"]

    class Meta:
        model = ProductReview

admin.site.register(ProductReview, ProductReviewAdmin)


class PreOrderProductFormAdmin(admin.ModelAdmin):
    list_display = ['id',"name", "email", "product"]

    class Meta:
        model = PreOrderProductForm

admin.site.register(PreOrderProductForm, PreOrderProductFormAdmin)
