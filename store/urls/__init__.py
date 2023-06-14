from django.urls import path, include

app_name = 'store'

urlpatterns = [
    # path('admin/', include('store.urls.admin'), name='admin.api'),
    path('public/', include('store.urls.public'), name='public.api')
]
