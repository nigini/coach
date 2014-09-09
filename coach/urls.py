from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^training/', include('training.urls', namespace='training')),
    url(r'^admin/', include(admin.site.urls)),
)
