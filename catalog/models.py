from django.db import models
from base.models import BaseModel, TaxTypes, CustomQuerySetManager,StructureChoices
from django.core.exceptions import  ValidationError
from django.utils.translation import gettext_lazy as _

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


    def _clean_standalone(self):
        """
        Validates a stand-alone category
        """
        if not self.title:
            raise ValidationError(_("Your Category must have a title."))
        if self.category_parent_id:
            raise ValidationError(_("Only child category can have a category parent."))

    def _clean_child(self):
        """
        Validates a child category
        """
        if not self.category_parent_id:
            raise ValidationError(_("A child category needs a parent."))
        if self.category_parent_id and not self.parent.is_parent:
            raise ValidationError(
                _("You can only assign child categories to parent categories."))

    def _clean_parent(self):
        """
        Validates a parent category.
        """
        self._clean_standalone()
        pass

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.attr.save()

    @property
    def is_standalone(self):
        return self.structure == self.STANDALONE

    @property
    def is_parent(self):
        return self.structure == self.PARENT

    @property
    def is_child(self):
        return self.structure == self.CHILD

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