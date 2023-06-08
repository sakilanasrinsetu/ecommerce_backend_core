from django.contrib import admin

from catalog.models import ProductGroup, Category, ProductBrand, TaxCategory

# Register your models here.

class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', "is_active","is_featured","show_in_ecommerce","ordering","created_at"]

    class Meta:
        model = ProductGroup

admin.site.register(ProductGroup, ProductGroupAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',"status" ,"product_group", "category_parent","is_active","is_featured","show_in_ecommerce","ordering","created_at"]

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)

class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',"is_active","is_featured","created_at"]

    class Meta:
        model = ProductBrand

admin.site.register(ProductBrand, ProductBrandAdmin)

class TaxCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',"is_active","value_in_percentage","type","created_at"]

    class Meta:
        model = TaxCategory

admin.site.register(TaxCategory, TaxCategoryAdmin)