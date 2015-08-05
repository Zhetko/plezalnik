from django.conf.urls import patterns, include, url
from django.contrib import admin
import plezalnikback.urls as purls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plezalnik.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(purls)),

)
