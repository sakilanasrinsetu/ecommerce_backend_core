from django.urls import path, include

app_name = 'catalog'

urlpatterns = [
    path('admin/', include('catalog.urls.admin'), name='admin.api'),
    path('public/', include('catalog.urls.public'), name='public.api'),

]
