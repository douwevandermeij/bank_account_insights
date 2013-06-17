import os
from django.conf import settings
from django.conf.urls import patterns, include, url
from geldzaken.core import urls as core_urls


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geldzaken.views.home', name='home'),
    # url(r'^geldzaken/', include('geldzaken.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += core_urls.urlpatterns

if settings.DEBUG:
    urlpatterns += patterns('',
       url(r'^%s/themes/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), 'django.views.static.serve',
           {'document_root': os.path.join(settings.MEDIA_ROOT, 'themes'), 'show_indexes': True}),
    )
