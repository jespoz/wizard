from django.conf.urls import patterns, url
from apps.security.views import ProfileView

urlpatterns = patterns('',
    url(regex=r'profile/$', view=ProfileView.as_view(), name='profile'),
)
