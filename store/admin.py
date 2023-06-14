from django.contrib import admin
from .models import *

# Register your models here.


class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'district']

    class Meta:
        model = Store

admin.site.register(Store, StoreAdmin)

class StorePaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', "store",'account_number']

    class Meta:
        model = StorePaymentMethod

admin.site.register(StorePaymentMethod, StorePaymentMethodAdmin)