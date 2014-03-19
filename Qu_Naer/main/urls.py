from django.conf.urls import patterns, include, url
from django.contrib import admin
import mapi
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Qu_Naer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mapi/', include(mapi.urls)),
)
