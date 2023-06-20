from django.db import models
from base.models import BaseModel

# Create your models here.


class POSUserAreas(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class POSUserRegions(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class POSProductInfo(models.Model):
    maximum_retail_price = models.FloatField(default=0.0)
    minimum_selling_price = models.FloatField(default=0.0)
    barcode_url = models.URLField(default="null", null=True, blank=True )
    commission_enabled = models.BooleanField(default=False)
    gsheba_amount = models.FloatField(default=0.0)
    pos_product_code = models.CharField(max_length=60)
    barcode = models.CharField(max_length=60)
    barcode_serial_number = models.PositiveIntegerField(default=0)
    restock_quantity = models.PositiveIntegerField( default=0)
    quantity_per_shop = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id)