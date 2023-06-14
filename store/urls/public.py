from django.urls import path
from store.views.public import PublicDistrictViewset
app_name = 'public'

urlpatterns = [
   #   path('district/', PublicDistrictViewset.as_view(
   #      {"get": "list"}),name="district"),
   #   path('district/<pk>/', PublicDistrictViewset.as_view(
   #      {"get": "retrieve"}),name="district"),

]