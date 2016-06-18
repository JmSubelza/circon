from django.conf.urls import patterns, url
from .views import Inventory
from .views import Oils
from .views import Rubbers
from .views import Uniforms
from .views import Stationery
from .views import Tools
from .views import SuppliesMedical

urlpatterns = patterns(' ',
                       url(r'^List_Inventory$', Inventory.as_view(),
                           name='list_inventory'),
                       url(r'^List_Oils$', Oils.as_view(), name='list_oils'),
                       url(r'^List_Rubbers$', Rubbers.as_view(),
                           name='list_rubbers'),
                       url(r'^List_Uniforms$', Uniforms.as_view(),
                           name='list_uniforms'),
                       url(r'^List_Stationery$', Stationery.as_view(),
                           name='list_stationery'),
                       url(r'^List_Tools$', Tools.as_view(),
                           name='list_tools'),
                       url(r'^List_SuppliesMedical$',
                           SuppliesMedical.as_view(),
                           name='list_suppliesmedical'),
                       )
