from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thehack.views.home', name='home'),
                       url(r'^mtest/', include('mtest.urls', namespace='mtest')),

    url(r'^admin/', include(admin.site.urls)),
)
