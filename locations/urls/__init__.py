from django.urls import path, include

app_name = 'locations'

urlpatterns = [
 
    path('public/', include('locations.urls.public'), name='public.api'),

]
