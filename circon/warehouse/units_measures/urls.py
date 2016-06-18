from django.conf.urls import patterns, url
from .views import DetailUnitsMeasures
from .views import ListUnitsMeasures
from .views import CreateUnitsMeasures
from .views import UpdateUnitsMeasures
from .views import DeleteUnitsMeasures

urlpatterns = patterns(' ',
                       url(r'^List_UnitsMeasures$',
                           ListUnitsMeasures.as_view(),
                           name='list_units_measures'),
                       url(r'^List_UnitsMeasures/Crear/$',
                           CreateUnitsMeasures.as_view(),
                           name='create_units_measures'),
                       url(r'^List_UnitsMeasures/Detail/(?P<pk>[0-9]+)/$',
                           DetailUnitsMeasures.as_view(),
                           name='detail_units_measures'),
                       url(r'^UnitsMeasures/Update/(?P<pk>[0-9]+)/$',
                           UpdateUnitsMeasures.as_view(),
                           name='update_units_measures'),
                       url(r'^UnitsMeasures/Delete/(?P<pk>[0-9]+)/$',
                           DeleteUnitsMeasures.as_view(),
                           name='delete_units_measures'),
                       )
