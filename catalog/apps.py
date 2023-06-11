from django.apps import AppConfig


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
    
    def ready(self):
        from actstream import registry
        registry.register(self.get_model('ProductGroup'))
        registry.register(self.get_model('Category'))
        registry.register(self.get_model('ProductBrand'))
        registry.register(self.get_model('TaxCategory'))
