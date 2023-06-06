from django.urls import path
from user.views.public import LoginViewSet

urlpatterns = [
    path('login/', LoginViewSet.as_view({'post':'create'}), name='login'),

]