from django.conf.urls import patterns, url
from .views import ListLogs


urlpatterns = patterns('', url(r'^ListLogs$', ListLogs.as_view(),
                               name='list_logs'),
                       )
