from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoPsaMongo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='home'),
)