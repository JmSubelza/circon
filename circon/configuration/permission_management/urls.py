from django.conf.urls import patterns, url
from .views import ListUsersPermission
from .views import UpdatePermission

urlpatterns = patterns(' ',
                       url(r'^List_Users_Permission$',
                           ListUsersPermission.as_view(),
                           name='list_permission'),
                       url(r'^Permission/Update/(?P<pk>[0-9]+)/$',
                           UpdatePermission.as_view(),
                           name='update_permission'),
                       )
