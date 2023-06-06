from django.urls import path, include

app_name = 'blogs'

urlpatterns = [
    path('admin/', include('blogs.urls.admin'), name='admin.api'),
    path('public/', include('blogs.urls.public'), name='public.api'),

]
