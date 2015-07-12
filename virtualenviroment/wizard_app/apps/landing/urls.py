from django.conf.urls import patterns, url
from apps.landing.views import LandingView

urlpatterns = patterns('',
    url(regex=r'$', view=LandingView.as_view(), name='landing'),
)
