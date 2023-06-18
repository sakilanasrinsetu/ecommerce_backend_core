from django.db import models
from base.models import BaseModel, TaxTypes, CustomQuerySetManager,StructureChoices
from django.core.exceptions import  ValidationError
from django.utils.translation import gettext_lazy as _
from discount.models import Discount
from gprojukti_v2.settings.app_vars import TODAY, CURRENT_TIME

# Create your models here.

class ProductGroup(BaseModel):
    name = models.CharField(max_length=255)
    translation = models.JSONField(default=dict)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    show_in_ecommerce = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)

    objects = CustomQuerySetManager.as_manager()

    """ For SEO Friendly for Operations """
    metaTitle = models.CharField(max_length=200)
    metaDescription = models.TextField(null=True, blank=True)
    canonical = models.URLField()
    banner_image = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['ordering']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_featured']),
            models.Index(fields=['ordering']),
        ]

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=255)
    translation = models.JSONField(default=dict)
    product_group = models.ForeignKey(ProductGroup,
                                      on_delete=models.CASCADE, 
                                      related_name='categories')
    translation = models.JSONField(default=dict)
    category_parent = models.ForeignKey('self',
                                on_delete=models.CASCADE,
                                null=True, blank=True,
                                related_name='categories',
                                help_text=_("Only choose a parent Category if you're creating a child "
                                "category.  For example if this is PC "
                                "3 of a particular [Normal, Gaming].  Leave blank if this is a "
                                "stand-alone Category (i.e. there is only one version of"
                                " this category).")
                    )
    slug = models.SlugField(max_length=255, unique=True)
    logo = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    show_in_ecommerce = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0) 
    featured_ordering = models.PositiveIntegerField(default=0) 
    status = models.CharField(max_length=20, choices=StructureChoices.choices)
    # ......***...... Note : Hide Because of Status Add ......***......
    # has_child = models.BooleanField(default=False) 

    """ For SEO Friendly for Operations """
    metaTitle = models.CharField(max_length=200,null=True, blank=True)
    metaDescription = models.TextField(null=True, blank=True)
    canonical = models.URLField(null=True, blank=True)
    banner_image = models.TextField(null=True, blank=True)
    is_child = models.BooleanField(default=False)
    discount = models.ForeignKey(Discount,
                                on_delete=models.CASCADE,
                                related_name='categories',
                                null=True, blank=True)

    class Meta:
        ordering = ['ordering']
        db_table = 'product_categories'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_featured']),
            models.Index(fields=['ordering']),
            models.Index(fields=['featured_ordering']),
        ]

    def __str__(self):
        return self.name

    # ....***.... For Status Automatically Setup  ....***....

    def generate_category_status(self):
        status = 'standalone'
        category_parent = None

        category_parent_status = None

        if self.category_parent:
            category_parent_status = self.category_parent.status

        category_parent_parent_id = None
        
        if self.status == 'standalone' and self.category_parent:
            category_parent = None
            

        elif self.status == 'parent' and self.category_parent:
            category_parent = None
            category_parent = None

        elif self.status == 'child' and not self.category_parent:
            status = 'standalone'
        
        
        elif self.status == 'child' and self.category_parent:
            category_parent_status = 'parent'
            category_parent_parent_id = None
            status = 'child'
            category_parent = self.category_parent


        return {
            "status": status,
            'category_parent': category_parent,
            'category_parent_status': category_parent_status,
            'category_parent_parent_id': category_parent_parent_id,
        }

    def save(self, *args, **kwargs):
        if not self == self.category_parent:
            obj = self.generate_category_status()
            self.status = obj.get('status')
            self.category_parent = obj.get('category_parent')

            if obj.get('category_parent'):
                self.category_parent.status = obj.get('category_parent_status')
                self.category_parent.category_parent = obj.get('category_parent_parent_id')

            if obj.get('status') == 'child' and obj.get('category_parent'):
                self.is_child = True
            else:
                self.is_child = False

            super().save(*args, **kwargs)
        pass

    # ....***.... For Status Automatically Setup  ....***....


class ProductBrand(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True)
    logo = models.URLField()
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)


    """ For SEO friendly Operations  """
    metaTitle = models.CharField(max_length=200)
    metaDescription = models.TextField(null=True, blank=True)
    canonical = models.URLField()

    class Meta:
        ordering = ['-created_at']
        db_table = 'product_brands'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_featured']),
        ]

    def __str__(self):
        return self.name
    
class TaxCategory(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=False, unique=True)
    value_in_percentage = models.FloatField()
    is_active = models.BooleanField(default=True)
    type = models.CharField(max_length=8, choices=TaxTypes.choices)

    class Meta:
        ordering = ['-created_at']
        db_table = 'tax_categories'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_active']),
            models.Index(fields=['value_in_percentage']),
        ]

    def __str__(self):
        return self.name

# ......***...... Note : Hide Because of Note Use ......***......

# class Attribute(BaseModel):
#     name = models.CharField(max_length=50)
#     translation = models.JSONField(default=dict)
#     group = models.ForeignKey(
#         ProductGroup, on_delete=models.CASCADE,
#         related_name='attributes')
#     category = models.ForeignKey(
#         Category, on_delete=models.CASCADE,
#         related_name='attributes')
#     # sub_category = models.ForeignKey(
#     #     to='catalog.ProductSubCategory', on_delete=models.CASCADE,
#     #     related_name='attributes')
#     description = models.TextField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     image_required = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['-created_at']
#         db_table = 'attributes'
#         indexes = [
#             models.Index(fields=['-created_at']),
#             models.Index(fields=['is_active']),
#         ]

#     def __str__(self):
#         return self.name


# class AttributeValue(BaseModel):
#     name = models.CharField(max_length=50)
#     attribute = models.ForeignKey(
#         to='catalog.Attribute', on_delete=models.CASCADE,
#         related_name='attribute_values')
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         ordering = ['-created_at']
#         db_table = 'attribute_values'
#         indexes = [
#             models.Index(fields=['-created_at']),
#             models.Index(fields=['is_active']),
#         ]

#     def __str__(self):
#         return self.name
