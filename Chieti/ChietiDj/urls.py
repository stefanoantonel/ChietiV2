from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ChietiDj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url('d/','proj2.tests.index',name='pro'),
    #url(r'$','proj2.tests.index'),
    url('index/','proj2.home.index',name='main'),
    
)
