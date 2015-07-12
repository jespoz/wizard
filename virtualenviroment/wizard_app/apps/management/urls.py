from django.conf.urls import patterns, url
from apps.management.views import ManagementView

urlpatterns = patterns('',
    url(regex=r'$', view=ManagementView.as_view(), name='management'),
)
