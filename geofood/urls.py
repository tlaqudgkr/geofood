from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.rest_list, name='rest_list'),
    url(r'^info/(?P<pk>\d+)/$', views.rest_detail, name='rest_detail'),
    url(r'^info/new/$', views.rest_new, name='rest_new'),
    url(r'^info/edit/(?P<pk>\d+)$', views.rest_edit, name='rest_edit'),
    url(r'^info/remove/(?P<pk>\d+)$', views.rest_remove, name='rest_remove')
]