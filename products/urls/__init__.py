from django.urls import path, include

app_name = 'products'

urlpatterns = [
    path('admin/', include('products.urls.admin'), name='admin.api'),
    path('public/', include('products.urls.public'), name='public.api'),

]
