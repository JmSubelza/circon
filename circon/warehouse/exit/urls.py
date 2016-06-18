from django.conf.urls import patterns, url
from circon.warehouse.exit.views import ListExit
from circon.warehouse.exit.views import CreateExit
from circon.warehouse.exit.views import DetailExitDetail
from circon.warehouse.exit.views import UpdateExit
from circon.warehouse.exit.views import DeleteExit
from circon.warehouse.exit.views import Confirm
from circon.warehouse.exit.views import Delivered
from circon.warehouse.exit.views import Cancel

urlpatterns = patterns(' ',
                       url(r'^List_Exit$', ListExit.as_view(),
                           name='list_exit'),
                       url(r'^Exit/Create/$', CreateExit.as_view(),
                           name='create_exit'),
                       url(r'^List_Exit/Detail/(?P<pk>[0-9]+)/$',
                           DetailExitDetail.as_view(), name='detail_exit'),
                       url(r'^Exit/Update/(?P<pk>[0-9]+)/$',
                           UpdateExit.as_view(),
                           name='update_exit'),
                       url(r'^Exit/Delete/(?P<pk>[0-9]+)/$',
                           DeleteExit.as_view(),
                           name='delete_exit'),
                       url(r'^Exit/Confirm/(?P<pk>[0-9]+)/$',
                           Confirm.as_view(),
                           name='confirm_exit'),
                       url(r'^Exit/Delivered/(?P<pk>[0-9]+)/$',
                           Delivered.as_view(),
                           name='delivered_exit'),
                       url(r'^Exit/Cancel/(?P<pk>[0-9]+)/$', Cancel.as_view(),
                           name='cancel_exit'),
                       )
