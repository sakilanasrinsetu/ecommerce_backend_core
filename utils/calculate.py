from discount.models import Discount
from gprojukti_v2.settings.app_vars import TODAY, CURRENT_TIME

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