from django.conf.urls import patterns, url, include
from rest_framework import routers
from .views import ProductsViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductsViewSet)

urlpatterns = patterns(' ',
                       url(r'^api/', include(router.urls)),
                       )
