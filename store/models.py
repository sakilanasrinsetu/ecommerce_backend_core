from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.postgres.fields import ArrayField

from base.models import BaseModel, PaymentMethodOptions, StoreTypeOptions
from point_of_sale.models import POSUserAreas, POSUserRegions
from locations.models import District


# Create your models here.

class Store(BaseModel):
    name = models.CharField(max_length=150)
    district = models.ForeignKey(District, on_delete=models.CASCADE,
                                related_name='stores', 
                                null=True, blank=True)
    type = models.CharField(max_length=12, 
                            choices=StoreTypeOptions.choices)
    slug = models.SlugField(max_length=255, null=False,
                            unique=True, blank=False)
    address = models.TextField(null=False)
    primary_phone = models.CharField(max_length=17)
    secondary_phone = models.CharField(max_length=17, blank=True, null=True)
    location = PointField(geography=True, default=Point(0.0, 0.0))
    map_link = models.URLField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    shown_in_website = models.BooleanField(default=True)
    off_days = ArrayField(models.CharField(max_length=15), default=list)
    is_active = models.BooleanField(default=True)
    area = models.ForeignKey(POSUserAreas, 
                            on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='stores')
    region = models.ForeignKey(POSUserRegions, 
                               on_delete=models.CASCADE,
                               null=True, blank=True,
                               related_name='stores')
    
    class Meta:
        ordering = ['-created_at']
        db_table = 'stores'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.name

    def latitude(self) -> float:
        return self.location.x

    def longitude(self) -> float:
        return self.location.y


class StorePaymentMethod(BaseModel):
    name = models.CharField(max_length=150)
    account_number = models.CharField(max_length=150)
    store = models.ForeignKey(Store,
                              on_delete=models.CASCADE,
                              related_name='store_payment_methods',
                              null=True, blank=True)
    type = models.CharField(
        max_length=15, choices=PaymentMethodOptions.choices)
    meta = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'store_payment_methods'
        indexes = [
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return self.name
