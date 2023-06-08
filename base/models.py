from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class BaseModel(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', _('active')
        INACTIVE = 'inactive', _('inactive')
        ARCHIVED = 'archived', _('archived')

    created_at = models.DateTimeField(auto_now_add=True,
                                      editable=False)
    updated_at = models.DateTimeField(auto_now=True,
                                      editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='created_%(class)ss')
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='updated_%(class)ss', null=True, blank=True)

    class Meta:
        abstract = True
        app_label = 'base'

    def save(self, *args, **kwargs):
        # Update the 'updated_at' field before saving the model
        self.updated_at = timezone.now()

        super(BaseModel, self).save(*args, **kwargs)


class CustomQuerySetManager(models.QuerySet):
    def filter_by_query(self,query_dict):
        return self.filter(**query_dict)


class TransferStatusTypes(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    PENDING = 'pending', 'pending'
    RECEIVED = 'received', 'received'
    REJECTED = 'rejected', 'rejected'


class TransactionTypes(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    PURCHASE_RETURN = 'purchase_return', 'purchase_return'
    PURCHASE = 'purchase', 'purchase'
    STORE_SELL = 'store_sell', 'store_sell'
    ECOMMERCE_SELL = 'ecommerce_sell', 'ecommerce_sell'
    ECOMMERCE_RETURN = 'ecommerce_return', 'ecommerce_return'
    TRANSFERRED_IN = 'transferred_in', 'transferred_in'
    TRANSFERRED_OUT = 'transferred_out', 'transferred_out'
    ADJUSTMENT = 'adjustment', 'adjustment'


class DiscountTypeChoices(models.TextChoices):
    FLAT = 'flat', _('flat')
    PERCENTAGE = 'percentage', _('percentage')


class BalanceTypes(models.TextChoices):
    PAID = 'paid', 'paid'
    DUE = 'due', 'due'


class PaymentMethodOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    CASH = 'cash', 'cash'
    BANK = 'bank', 'Bank'
    CARD = 'card', 'card'
    MOBILE_BANK = 'mobile_bank', 'mobile_bank'


class TaxTypes(models.TextChoices):
    SELL_TAX = 'sell_tax', 'sell_tax'
    BUY_TAX = 'buy_tax', 'buy_tax'


class CompanyTypeOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    LOCAL = 'local', 'local'
    FOREIGN = 'foreign', 'foreign'


class StockAdjustmentReasonOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    DAMAGE_GOODS = 'damage_goods', 'damage_goods'
    WRONG_ENTRY = 'wrong_entry', 'wrong_entry'


class OrderStatusOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    PENDING = 'pending', 'pending'
    AVAILABILITY_CHECK = 'availability_check', 'availability_check'
    QUALITY_CONTROL = 'quality_control', 'quality_control'
    PACKAGING = 'packaging', 'packaging'
    CONFIRMED_ORDER = 'confirmed_order', 'confirmed_order'
    DISPATCHED = 'dispatched', 'dispatched'
    DELIVERED = 'delivered', 'delivered'
    STORE_SELL = 'store_sell', 'store_sell'
    SHIPMENT_READY = 'shipment_ready', 'shipment_ready'
    CANCELLED = 'cancelled', 'cancelled'


class PaymentTypeOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    CASH_ON_DELIVERY = 'cash_on_delivery', 'cash_on_delivery'
    ONLINE_PAYMENT = 'online_payment', 'online_payment'
    PAY_AT_SHOP = 'pay_at_store', 'pay_at_store'


class PaymentStatusOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    UNPAID = 'unpaid', 'unpaid'
    PAID = 'paid', 'paid'
    DUE = 'due', 'due'


class DeliveryOptions(models.TextChoices):
    HOME_DELIVERY = 'home_delivery', ('home_delivery')
    STORE_PICKUP = 'store_pickup', ('store_pickup')
    STORE_SALE = 'store_sale', ('store_sale')


class StoreTypeOptions(models.TextChoices):
    STORE = 'store', ('store')
    WAREHOUSE = 'warehouse', ('warehouse')


class WarrantyDurationOptions(models.TextChoices):
    DAY = 'day', ('day')
    MONTH = 'month', ('month')
    YEAR = 'year', ('year')



class OnlinePaymentMethodOptions(models.TextChoices):
    SSL_ECOMMERCE = 'ssl_ecommerce', 'ssl_ecommerce'


class OnlinePaymentStatusOptions(models.TextChoices):
    INITIATED = 'initiated', 'initiated'
    COMPLETED = 'completed', 'completed'
    CANCELLED = 'cancelled', 'cancelled'
    REJECTED = 'rejected', 'rejected'
    VALID = 'failed', 'failed'
    PAID = 'paid', 'paid'


class PromoTypeOptions(models.TextChoices):
    GENERAL = 'general', 'general'
    USER_SPECIFIC = 'user_specific', 'user_specific'


class OrderIssueStatusOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    SUBMITTED = 'submitted', 'submitted'
    ACCEPTED = 'accepted', 'accepted'
    REJECTED = 'rejected', 'rejected'
    RESOLVED = 'resolved', 'resolved'


class FAQTypeOptions(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    GENERAL = 'general', 'general'
    REPAIR = 'repair', 'repair'


class OrderCustomerType(models.TextChoices):
    REGULAR = 'regular', _('regular')
    CORPORATE = 'corporate', _('corporate')


class DeliveryChargeCityTypeOptions(models.TextChoices):
    INSIDE_DHAKA = 'inside_dhaka', _('inside_dhaka')
    OUTSIDE_DHAKA = 'outside_dhaka', _('outside_dhaka')


class StructureChoices(models.TextChoices):
    """ CONSTANT = DB_VALUE, USER_DISPLAY_VALUE """
    STANDALONE = 'standalone', 'Stand-alone category'
    PARENT = 'parent', 'Parent'
    CHILD = 'child', 'Child'