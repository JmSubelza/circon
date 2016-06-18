from django.conf.urls import patterns, url

urlpatterns = patterns('circon.configuration.authenticate.views',
                       url(r'^login/$', 'login_view', name='view_login'),
                       url(r'^logout/$', 'logout_view', name='view_logout'),
                       )
