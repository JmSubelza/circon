from django.conf.urls import patterns, url
from .views import ListTranslationPermission
from .views import UpdateTranslationPermission

urlpatterns = patterns(' ',
                       url(r'^List/TranslationPermission$',
                           ListTranslationPermission.as_view(),
                           name='list_translationpermission'),
                       url(r'^Permission/Translation/Update/(?P<pk>[0-9]+)/$',
                           UpdateTranslationPermission.as_view(),
                           name='update_translationpermission'),
                       )
