from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ChietiDj.views.home', name='home'),
    url(r'home/', 'chieti.views.home', name='home'),
    url(r'head/', 'chieti.mainHead.index', name='head'),
    url(r'addProduct/', 'chieti.views.addProd', name='addProd'),
    url(r'addProduct2/', 'chieti.views.addProd2', name='addProd2'),
    #url(r'^admin/', include(admin.site.urls)),
    #url('d/','chieti.tests.index',name='pro'),
    #url(r'$','chieti.tests.index'),
    #url('index/',include('chieti.urls')),
    url(r'product/','chieti.views.showProduct'),
    url(r'changePrice/','chieti.views.changePrice'),
    url(r'changePrice2/','chieti.views.changePrice2'),
    url(r'addToOrder/','chieti.views.addToOrder'),
    url(r'changeOrder/','chieti.views.changeOrder'),
    url(r'changeOrder2/','chieti.views.changeOrder2'),
    url(r'removeItem/','chieti.views.removeItem'),

    
)

