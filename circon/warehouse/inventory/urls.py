from django.conf.urls import patterns, url
from .views import Inventory
from .views import SearchCategory


urlpatterns = patterns(' ',
                       url(r'^List_Inventory$', Inventory.as_view(),
                           name='list_inventory'),
                       url(r'^/SearchCategory/(?P<pk>[0-9]+)/$', SearchCategory.as_view(),
                           name='search_category'),
                       )
