from django.urls import path
from store.views.public import PublicStoreViewset
app_name = 'public'

urlpatterns = [
     path('store/', PublicStoreViewset.as_view(
        {"get": "list"}),name="store"),
     path('store/<slug>/', PublicStoreViewset.as_view(
        {"get": "retrieve"}),name="store"),

]