"""gprojukti_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,  re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework import permissions
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import routers

from gprojukti_v2.views import (HealthCheckViewset)

router = routers.DefaultRouter()



schema_urlpatterns = [
    path("spectacular/", SpectacularAPIView.as_view(), name="schema"),
    path("",SpectacularSwaggerView.as_view(url_name="schema"),name="doc",),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"),name="redoc",),
]

v2_patterns = [
    path('users/', include('user.urls', namespace='user.apis')),
    path('catalog/', include('catalog.urls', namespace='catalog.apis')),
    path('products/', include('products.urls', namespace='products.apis')),
    path('store/', include('store.urls', namespace='store.apis')),
    path('discount/', include('discount.urls', namespace='discount.apis')),
    # path('supplier/', include('supplier.urls', namespace='supplier.apis')),
    # path('campaigns/', include('campaigns.urls', namespace='campaigns.apis')),
    # path('configuration/', include('configuration.urls', namespace='configuration.apis')),
    # path('stock/', include('stock.urls', namespace='stock.apis')),
    # path('purchase/', include('purchase.urls', namespace='purchase.apis')),
    path('blogs/', include('blogs.urls', namespace='blogs.apis')),
    # path('sell/', include('orders.urls', namespace='orders.apis')),
    # path('payment/', include('payment.urls', namespace='payment.apis')),
    # path('promo/', include('promo.urls', namespace='promo.apis')),
    # path('repair/', include('repair.urls', namespace='repair.apis')),
    # path('pc_builder/', include('pc_builder.urls', namespace='pc_builder.apis')),
    # path('pos/', include('point_of_sale.urls', namespace='point_of_sale.apis')),
    path('locations/', include('locations.urls', namespace='locations.apis')),
    # path('image-upload', image_upload),
    # path('ordering-update', ordering_update),
    # path('featured-ordering-update', featured_ordering_update),

]

urlpatterns = [
        path('admin/', admin.site.urls),
        # path('health_check/', health_check),
        path('health_check/', HealthCheckViewset.as_view({"get": "health_check"}),
                      name="health_check"),
        path('api/', include([
        path('v2.0/', include(v2_patterns))
                  ])),
        path('api-auth/', include('rest_framework.urls')),

              ] + schema_urlpatterns

if settings.DEBUG:
    urlpatterns = urlpatterns + \
                  static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
                  static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)

