from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbrelease.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$',  'dbrelease_app.views.login'),
    (r'^accounts/logout/$', 'dbrelease_app.views.logout'),
)
