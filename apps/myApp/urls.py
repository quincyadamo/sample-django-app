from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^travels/trip_add$', views.trip_add, name='trip_add'),
    url(r'^travels/add$', views.travels_add, name='travels_add'),
    url(r'^travels/destination/(?P<id>\d+)$', views.travels_destination, name='travels_destination'),
    url(r'^travels/join/(?P<id>\d+)$', views.trip_join, name='trip_join'),
    url(r'^travels$', views.travels, name='travels')
]
