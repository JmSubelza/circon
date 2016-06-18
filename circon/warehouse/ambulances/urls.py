from django.conf.urls import patterns, url
from .views import DetailAmbulances
from .views import ListAmbulances
from .views import CreateAmbulances
from .views import UpdateAmbulances
from .views import DeleteAmbulances

urlpatterns = patterns(' ',
                       url(r'^List_Ambulances$', ListAmbulances.as_view(),
                           name='list_ambulances'),
                       url(r'^List_Ambulances/Crear/$',
                           CreateAmbulances.as_view(),
                           name='create_ambulances'),
                       url(r'^List_Ambulances/Detail/(?P<pk>[0-9]+)/$',
                           DetailAmbulances.as_view(),
                           name='detail_ambulances'),
                       url(r'^Ambulances/Update/(?P<pk>[0-9]+)/$',
                           UpdateAmbulances.as_view(),
                           name='update_ambulances'),
                       url(r'^Ambulances/Delete/(?P<pk>[0-9]+)/$',
                           DeleteAmbulances.as_view(),
                           name='delete_ambulances'),
                       )
