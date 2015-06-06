from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import Home

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)
