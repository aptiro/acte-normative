from django.conf.urls import patterns, include, url
from django.contrib import admin

from bills import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^receive_bills$', views.receive_bills),
    url(r'^crashme$', views.crashme),
)
