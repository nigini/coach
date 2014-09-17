from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^training/', include('training.urls', namespace='training')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'training/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/training/team/'}, name='logout'),
)
