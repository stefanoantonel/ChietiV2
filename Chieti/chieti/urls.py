from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ChietiDj.views.home', name='home'),
    url(r'home/', 'chieti.views.home', name='home'),
    url(r'head/', 'chieti.mainHead.index', name='head'),
    url(r'addProduct/', 'chieti.views.addProd', name='addProd'),

    url(r'addProduct2/', 'chieti.views.addProd2', name='addProd2'),

    url(r'hom/ad/', 'chieti.views.addProd2', name='addProd2'),
    
   


    #url(r'^admin/', include(admin.site.urls)),
    #url('d/','chieti.tests.index',name='pro'),
    #url(r'$','chieti.tests.index'),
    #url('index/',include('chieti.urls')),
    url(r'product/','chieti.views.showProduct'),
    url(r'changePrice/','chieti.views.changePrice'),
    url(r'changePrice2/','chieti.views.changePrice2'),
    url(r'addToOrder/','chieti.views.addToOrder'),
    url(r'mainHead/','chieti.views.mainHead'),
    
    url(r'sales/','chieti.views.showSales'),

    url(r'changeOrder/','chieti.views.changeOrder'),
    url(r'changeOrder2/','chieti.views.changeOrder2'),
    url(r'removeItem/','chieti.views.removeItem'),
    url(r'summaryBuy/','chieti.views.summaryBuy'),
    url(r'printOrders/','chieti.views.printOrders'),
    url(r'cancelProduct/','chieti.views.cancelProduct'),
    url(r'cancelProduct2/','chieti.views.cancelProduct2'),
    url(r'singUp/','chieti.views.singUp'),
    url(r'sendMail/','chieti.views.sendMail'),
    url(r'singUp2/','chieti.views.singUp2'),
    url(r'singUp3/','chieti.views.singUp3'),
    
	url(r'init/','chieti.views.init'),
	url(r'singUpFake/','chieti.views.singUpFake'),
	url(r'singUp2Fake/','chieti.views.singUp2Fake'),
	url(r'test/','chieti.views.test'),
	url(r'changeUser/','chieti.views.changeUser'),
	
	

)

