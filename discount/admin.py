from django.contrib import admin
from discount.models import Discount

# Register your models here.

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','discount_type','discount_schedule_type', 'is_active']
    list_display = ['id', 'name','discount_type','discount_schedule_type', 'is_active']

    class Meta:
        model = Discount

admin.site.register(Discount, DiscountAdmin)
