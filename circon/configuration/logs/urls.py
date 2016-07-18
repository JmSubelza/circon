from django.conf.urls import patterns, url
from .views import ListLogs
from .views import LogsProducts


urlpatterns = patterns('',
                       url(r'^ListLogs$', ListLogs.as_view(),
                           name='list_logs'),
                       url(r'^LogsProducts$', LogsProducts.as_view(),
                           name='logs_products'),
                       )
