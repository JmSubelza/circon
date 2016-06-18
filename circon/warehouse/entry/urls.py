from django.conf.urls import patterns, url
from circon.warehouse.entry.views import ListEntry
from circon.warehouse.entry.views import CreateEntry
from circon.warehouse.entry.views import DetailEntryDetail
from circon.warehouse.entry.views import UpdateEntry
from circon.warehouse.entry.views import DeleteEntry
from circon.warehouse.entry.views import Confirm
from circon.warehouse.entry.views import Cancel

urlpatterns = patterns(' ',
                       url(r'^List_Entry$', ListEntry.as_view(),
                           name='list_entry'),
                       url(r'^Entry/Create/$', CreateEntry.as_view(),
                           name='create_entry'),
                       url(r'^List_Entry/Detail/(?P<pk>[0-9]+)/$',
                           DetailEntryDetail.as_view(),
                           name='detail_entry'),
                       url(r'^Entry/Update/(?P<pk>[0-9]+)/$',
                           UpdateEntry.as_view(), name='update_entry'),
                       url(r'^Entry/Delete/(?P<pk>[0-9]+)/$',
                           DeleteEntry.as_view(),
                           name='delete_entry'),
                       url(r'^Entry/Confirm/(?P<pk>[0-9]+)/$',
                           Confirm.as_view(),
                           name='confirm_entry'),
                       url(r'^Entry/Cancel/(?P<pk>[0-9]+)/$', Cancel.as_view(),
                           name='cancel_entry'),
                       )
