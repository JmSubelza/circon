from django.conf.urls import patterns, url
from .views import Inventory


urlpatterns = patterns(' ',
                       url(r'^List_Inventory$', Inventory.as_view(),
                           name='list_inventory'),
                       )
