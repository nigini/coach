from django.conf.urls import patterns, url
from training import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^team/$', views.get_athletes_list, name='athletes_list'),
    url(r'^athletes/(?P<athlete_id>\d+)/$', views.get_athlete, name='athlete'),
    url(r'^athletes/(?P<athlete_id>\d+)/feedback/(?P<activity_id>\d+)/$', views.feedback, name='feedback'),

    #TEMP
    url(r'^(?P<athlete_name>\w+)/$', views.index, name='index_name'),
)