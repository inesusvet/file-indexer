from django.conf.urls import patterns, include, url
from django.contrib import admin

from video.views import *

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^search/$', SearchResultsView.as_view(), name='search_results'),

    url(r'^admin/', include(admin.site.urls)),
)
