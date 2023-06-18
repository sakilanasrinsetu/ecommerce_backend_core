from django.apps import AppConfig


class DiscountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'discount'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Discount'))

