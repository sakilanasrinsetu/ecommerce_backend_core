from discount.models import Discount
from ecommerce_core.settings.app_vars import TODAY, CURRENT_TIME

def valid_discount(discount_obj, **kwargs):
    is_valid = False

    if discount_obj:
        if discount_obj.discount_schedule_type == 'date_wise':
            if discount_obj.start_date.date() <= TODAY.date() and discount_obj.end_date.date() >= TODAY.date():
                is_valid = True

        elif discount_obj.discount_schedule_type == 'time_wise':
            if discount_obj.start_time <= CURRENT_TIME and discount_obj.end_time >= CURRENT_TIME:
                is_valid = True


    return is_valid

def calculate_discount_price(selling_price, discount_obj, **kwargs):
    
    discounted_price = None

    if discount_obj:
        if discount_obj.discount_type == 'percentage':
            discounted_price =selling_price - ((selling_price*discount_obj.amount)/100)

        else:
            discounted_price =selling_price - discount_obj.amount

    return discounted_price