from django.db import models
from base.models import BaseModel, DeliveryChargeCityTypeOptions, FAQTypeOptions


class TermsAndConditions(BaseModel):
    header = models.CharField(max_length=150, unique=True)
    conditions = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'terms_and_conditions'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.header


class Banner(BaseModel):
    name = models.CharField(max_length=150)
    url = models.URLField()
    image = models.URLField()
    size = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering']
        db_table = 'banners'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.name


class Faq(BaseModel):
    title = models.CharField(max_length=250)
    translation = models.JSONField(default=dict)
    description = models.TextField()
    type = models.CharField(
        max_length=8, choices=FAQTypeOptions.choices, default=FAQTypeOptions.GENERAL)
    ordering = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['ordering']
        db_table = 'faqs'
        indexes = [
            models.Index(fields=['ordering']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.title


class Courier(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    address = models.TextField()
    meta = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        db_table = 'courier'
        indexes = [
            models.Index(fields=['-created_at']),
        ]


class NewsletterSubscriber(models.Model):
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
        db_table = 'newsletter_subscribers'
        indexes = [
            models.Index(fields=['email']),
        ]


class DeliveryCharge(models.Model):
    city_type = models.CharField(
        max_length=20, choices=DeliveryChargeCityTypeOptions.choices)
    amount = models.FloatField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'delivery_charges'
        indexes = [
            models.Index(fields=['city_type']),
        ]


class Seller(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'sellers'
