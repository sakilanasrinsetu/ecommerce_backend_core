from django.contrib import admin
from point_of_sale.models import POSProductInfo,POSUserRegions, POSUserAreas

# Register your models here.
class POSUserAreasAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    class Meta:
        model = POSUserAreas

admin.site.register(POSUserAreas, POSUserAreasAdmin)

class POSUserRegionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    class Meta:
        model = POSUserRegions

admin.site.register(POSUserRegions, POSUserRegionsAdmin)

class POSProductInfoAdmin(admin.ModelAdmin):
    list_display = ['id']

    class Meta:
        model = POSProductInfo

admin.site.register(POSProductInfo, POSProductInfoAdmin)