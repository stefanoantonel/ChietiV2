from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ChietiDj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url('d/','chieti.tests.index',name='pro'),
    #url(r'$','chieti.tests.index'),
    url('chieti/',include('chieti.urls')),
    url(r'^accounts/', include('allauth.urls')),
    
)
