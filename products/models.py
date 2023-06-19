from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from base.models import BaseModel, WarrantyDurationOptions
from point_of_sale.models import POSProductInfo
from configuration.models import Seller
from base.models import BaseModel,StructureChoices
from django.utils.translation import gettext_lazy as _
from catalog.models import Category, ProductBrand, TaxCategory
from store.models import Store
from django.contrib.postgres.fields import ArrayField
from discount.models import Discount
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
import re
from utils.generates import unique_slug_generator



# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150, unique=True)

    # ....***.... Note: Status Add for single Model
    status = models.CharField(max_length=20, 
                              choices=StructureChoices.choices)
    parent_product = models.ForeignKey('self',
                                on_delete=models.CASCADE,
                                null=True, blank=True,
                                related_name='products',
                                help_text=_("Only choose a parent Product if you're creating a child "
                                "Product.  For example if this is PC "
                                "3 of a particular [Normal, Gaming].  Leave blank if this is a "
                                "stand-alone Category (i.e. there is only one version of"
                                " this Product).")
                    )

    """  For SEO Friendly """
    metaTitle = models.CharField(max_length=200, null=True, blank=True)
    metaDescription = models.TextField(null=True, blank=True)
    canonical = models.URLField( null=True, blank=True)
    ogImage = models.URLField(null=True, blank=True)
    ogTitle = models.CharField(max_length=200, null=True, blank=True)
    ogDescription = models.TextField(null=True, blank=True)

 
    description = models.TextField()
    selling_tax_category = models.ForeignKey(
        to=TaxCategory, 
        on_delete=models.CASCADE, related_name='selling_products')
    buying_tax_category = models.ForeignKey(
        to=TaxCategory, 
        on_delete=models.CASCADE, related_name='buying_products')
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    # ....***.... After Marge ....***....

    brand = models.ForeignKey(ProductBrand, 
                              on_delete=models.CASCADE,
                              related_name='products')
    images = models.JSONField(default=list)
    sku = models.CharField(max_length=100, null=False, unique=True)
    categories = models.ManyToManyField(Category, 
                                        related_name='category_products')
    sub_categories = models.ManyToManyField(Category,
                                            related_name='sub_category_products')
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
    pos_product_info = models.ForeignKey(POSProductInfo, 
                                        on_delete=models.CASCADE,
                                        null=True, blank=True,
                                        related_name='products')
    discount = models.ForeignKey(Discount,
                                on_delete=models.CASCADE,
                                related_name='products',
                                null=True, blank=True)

  
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
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='product_sellers')
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE,
        related_name='product_sellers')


    def __str__(self):
        if self.product_variant:
            return self.product_variant.name
        return str(self.pk)

class ProductReview(BaseModel):
    product = models.ForeignKey(Product,
                                 on_delete=models.CASCADE,
                                 related_name='product_reviews',
                                 null=True, blank=True)
    
    #TODO: When Order Model Add Then Add This Key

    # order = models.ForeignKey(to='orders.Order',
    #                             on_delete=models.CASCADE, 
    #                             related_name='product_reviews',
    #                             null=True, blank=True)
    
    review = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    is_accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        db_table = 'product_reviews'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['rating']),
        ]

    def __str__(self):
        return str(self.rating)
    
# class ProductAttribute(BaseModel):
#     product = models.ForeignKey(Product,
#                                 on_delete=models.CASCADE,
#                                 related_name='product_attributes',
#                                 null=True, blank=True)
#     attribute = models.ForeignKey(Attribute,
#                                    on_delete=models.CASCADE,
#                                    related_name='product_attributes',
#                                    null=True, blank=True)
#     attribute_value = models.ForeignKey(AttributeValue,
#                                          on_delete=models.CASCADE,
#                                          related_name='product_attributes',
#                                          null=True, blank=True)

#     class Meta:
#         ordering = ['-created_at']
#         db_table = 'product_variant_attributes'
#         indexes = [
#             models.Index(fields=['-created_at']),
#         ]

#     def __str__(self):
#         return str(self.product)

# ***NOTE***: Product Serial Remove Because of Does not Used
    

class PreOrderProductForm(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    product = models.ForeignKey(Product, 
                                on_delete=models.CASCADE,
                                related_name='pro_order_product_forms',
                                null=True, blank=True)
    quantity = models.IntegerField(default=1,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

 # TODO: Here In Store Key FK Relation Setup

class TransferProduct(models.Model):
    from_store = models.ForeignKey(Store, on_delete=models.CASCADE,
                                   related_name='from_transfer_products',
                                   null=True, blank=True)
    to_store = models.ForeignKey(Store, on_delete=models.CASCADE,
                                   related_name='to_transfer_products',
                                   null=True, blank=True)
    sku_list = ArrayField(models.CharField(max_length=200), null=True)
    approval_status = models.CharField(max_length=200, null=True,default=False)
    date = models.DateTimeField(auto_now_add=True)


# def product_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    
#     if not instance.slug:
#         title = slugify(instance.name.lower())
#         slug_binding = title + '-' + unique_slug_generator()
#         instance.slug = title

# pre_save.connect(product_slug_pre_save_receiver, sender=Product)