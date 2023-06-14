from django.contrib import admin
from .models import Division, District, Area, StoreLocation

# Register your models here.

class DivisionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]

    class Meta:
        model = Division

admin.site.register(Division, DivisionAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]

    class Meta:
        model = District

admin.site.register(District, DistrictAdmin)


class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',"district"]

    class Meta:
        model = Area

admin.site.register(Area, AreaAdmin)


class StoreLocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]

    class Meta:
        model = StoreLocation

admin.site.register(StoreLocation, StoreLocationAdmin)