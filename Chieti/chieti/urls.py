from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ChietiDj.views.home', name='home'),
    url(r'home/', 'chieti.views.home', name='home'),
    url(r'head/', 'chieti.mainHead.index', name='head'),
    url(r'addProduct/', 'chieti.views.addProd', name='addProd'),
    url(r'hom/ad/', 'chieti.views.addProd2', name='addProd2'),
    #url(r'^admin/', include(admin.site.urls)),
    #url('d/','chieti.tests.index',name='pro'),
    #url(r'$','chieti.tests.index'),
    #url('index/',include('chieti.urls')),
    
)

