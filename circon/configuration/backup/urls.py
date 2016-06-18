from django.conf.urls import patterns, url
from .views import Backup


urlpatterns = patterns('', url(r'^Backup$', Backup.as_view(),
                               name='backup'),
                       )
