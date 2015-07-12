from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.security.views import AdministratorRegister

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', AdministratorRegister.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^management/', include('apps.management.urls')),
    url(r'^security/', include('apps.security.urls')),
    url(r'^', include('apps.landing.urls')),
)
