from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import Home

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
