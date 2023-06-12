from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from base.models import BaseModel, WarrantyDurationOptions
# from point_of_sale.models import POSProductInfo
from configuration.models import Seller

# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150, unique=True)

    """  For SEO Friendly """
    metaTitle = models.CharField(max_length=200, null=True, blank=True)
    metaDescription = models.TextField(null=True, blank=True)
    canonical = models.URLField( null=True, blank=True)
    ogImage = models.URLField(null=True, blank=True)
    ogTitle = models.CharField(max_length=200, null=True, blank=True)
    ogDescription = models.TextField(null=True, blank=True)

 
    description = models.TextField()
    selling_tax_category = models.ForeignKey(
        to='catalog.TaxCategory', 
        on_delete=models.CASCADE, related_name='selling_products')
    buying_tax_category = models.ForeignKey(
        to='catalog.TaxCategory', 
        on_delete=models.CASCADE, related_name='buying_products')
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    # ....***.... After Marge ....***....

    brand = models.ForeignKey(to='catalog.ProductBrand', 
                              on_delete=models.CASCADE,
                              related_name='products')
    images = models.JSONField(default=list)
    sku = models.CharField(max_length=100, null=False, unique=True)
    categories = models.ManyToManyField('catalog.Category', related_name='category_products')
    sub_categories = models.ManyToManyField('catalog.Category',related_name='sub_category_products')
    translation = models.JSONField(default=dict)
    images = models.JSONField(default=list)
    selling_price = models.FloatField()
    specifications = models.JSONField(default=dict)
    meta = models.JSONField(default=dict)
    online_discount = models.JSONField(default=dict)
    offline_discount = models.JSONField(default=dict)
    service_warranty = models.PositiveIntegerField()
    service_warranty_duration_type = models.CharField(
        max_length=20, choices=WarrantyDurationOptions.choices, null=True)
    sell_warranty = models.PositiveIntegerField()
    sell_warranty_duration_type = models.CharField(
        max_length=20, choices=WarrantyDurationOptions.choices, null=True)
    minimum_stock_quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_top_sale = models.BooleanField(default=False)
    is_upcoming = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    show_on_landing_page = models.BooleanField(default=False)
    show_in_ecommerce = models.BooleanField(default=True)
    on_the_go = models.BooleanField(default=False)
    is_special_day = models.BooleanField(default=False)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    integrity_guaranteed = models.JSONField(default=dict)
    ordering = models.PositiveIntegerField(default=0)
    sellers = models.ManyToManyField(
        Seller, through='ProductSeller', related_name='products')
    banner_message = models.TextField(null=True, blank=True)
    metaTitle = models.CharField(max_length=200, null=True, blank=True)
    metaDescription = models.TextField(null=True, blank=True)
    canonical = models.CharField(max_length=200,null=True, blank=True)
    ogImage = models.TextField(null=True, blank=True)
    ogTitle = models.CharField(max_length=200, null=True, blank=True)
    ogDescription = models.TextField(null=True, blank=True)
    ogUrl = models.CharField(max_length=200,null=True, blank=True)
    is_only_pos = models.BooleanField(default=False)
    # pos_product_info = models.ForeignKey(POSProductInfo, 
    #                                     on_delete=models.CASCADE,
    #                                       null=True, blank=True,
    #                                       related_name='products')
  
    class Meta:
        ordering = ['ordering']
        db_table = 'product_variants'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_featured']),
            models.Index(fields=['is_top_sale']),
            models.Index(fields=['minimum_stock_quantity']),
            models.Index(fields=['name']),
            models.Index(fields=['ordering']),
        ]

class ProductSeller(models.Model):
    product_variant = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='product_sellers')
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE,
        related_name='product_sellers')


    def __str__(self):
        if self.product_variant:
            return self.product_variant.name
        return str(self.pk)