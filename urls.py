from django.conf.urls import patterns, include, url
from pydetector.views import hello

from pydetector.views2 import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^logs/$', logs),
    # Examples:
     url(r'^$', welcome),
    # url(r'^pydetector/', include('pydetector.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
