from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from inventory import api

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Djember.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'inventory.views.home'),

    #Endpoints
    url(r'^api/productos/$', api.ProductoList.as_view()),
    url(r'^api/productos/(?P<pk>[0-9]+)/$', api.ProductoDetail.as_view()),
    url(r'^api/proveedores/$', api.ProveedorList.as_view()),
    url(r'^api/proveedores/(?P<pk>[0-9]+)/$', api.ProveedorDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
