from django.db import models
from base.models import DiscountTypeChoices, DiscountScheduleTypeChoices
from django.utils import timezone
from datetime import date, datetime, timedelta


# Create your models here.

class Discount(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    discount_schedule_type = models.CharField(choices=DiscountScheduleTypeChoices.choices,
                                              max_length=50, default="date_wise")
    discount_type = models.CharField(choices=DiscountTypeChoices.choices,
                                     max_length=50, default="flat")

    amount = models.FloatField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

    # ***NOTE*** Discount Basic Validation Check 
    
    def generate_discount_active(self):
        is_active = False

        today = datetime.strptime(
                str(timezone.datetime.now().date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
            )
        current_time = timezone.datetime.now().time()

        if self.discount_schedule_type == 'date_wise':
            if self.start_date.date() <= today.date() and self.end_date.date() >= today.date():
                is_active = True

        elif self.discount_schedule_type == 'time_wise':
            if self.start_time <= current_time and self.end_time >= current_time:
                is_active = True

        return {
            'is_active':is_active
        }
    
    def save(self, *args, **kwargs):
        if self.discount_type == 'percentage' and self.amount > 100:
            self.is_active = False
        else:    
            obj = self.generate_discount_active()
            self.is_active = obj.get('is_active')

        super().save(*args, **kwargs)



        