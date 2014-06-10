from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'chieti.views.home', name='home'),
    #url('','chieti.views.home'),
    url(r'home', 'chieti.views.home', name='home'),
    url(r'homa/', 'chieti.views.homa', name='home'),
    url(r'quienes/', 'chieti.views.quienes', name='home'),
    url(r'comoComprar/', 'chieti.views.comoComprar', name='home'),
    url(r'head/', 'chieti.mainHead.index', name='head'),
    url(r'addProduct/', 'chieti.views.addProd', name='addProd'),

    url(r'addProduct2/', 'chieti.views.addProd2', name='addProd2'),

    url(r'hom/ad/', 'chieti.views.addProd2', name='addProd2'),
    
    url(r'auto', 'chieti.views.auto', name='addProd2'),
    url(r'complete', 'chieti.views.complete', name='addProd2'),
    url(r'compCategory', 'chieti.views.compCategory', name='addProd2'),
    
    #url(r'^admin/', include(admin.site.urls)),
    #url('d/','chieti.tests.index',name='pro'),
    #url(r'$','chieti.tests.index'),
    #url('index/',include('chieti.urls')),
    url(r'product/','chieti.views.showProduct', name='productos'),
    url(r'bienvenido/','chieti.views.bienvenido'),
    url(r'changePrice/','chieti.views.changePrice'),
    url(r'changePrice2/','chieti.views.changePrice2'),
    url(r'addToOrder/','chieti.views.addToOrder'),
    url(r'mainHead/','chieti.views.mainHead'),
    
    url(r'sales/','chieti.views.showSales'),

    url(r'changeOrder/','chieti.views.changeOrder'),
    url(r'changeOrder2/','chieti.views.changeOrder2'),
    url(r'changeOrder3/','chieti.views.changeOrder3'),
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
	url(r'changeUser2/','chieti.views.changeUser2'),
	
	url(r'test1','chieti.views.test1'),
	url(r'singIn/','chieti.views.singIn'),
	url(r'singIn2/','chieti.views.singIn2'),
	url(r'markDelivered/','chieti.views.markDelivered'),
	url(r'changeProduct/','chieti.views.changeProduct'),
	url(r'changeProduct2/','chieti.views.changeProduct2'),
	url(r'usernameExist/','chieti.views.usernameExist'),
	
	
	url(r'changePass0/','chieti.views.changePass0'),
	url(r'changePass1/','chieti.views.changePass1'),
	url(r'changePass2/','chieti.views.changePass2'),
	url(r'changePass3/','chieti.views.changePass3'),
	url(r'changeUserData/','chieti.views.changeUserData'),
	url(r'changeUserData2/','chieti.views.changeUserData2'),
	url(r'adm/','chieti.views.adm'),
    url(r'findProductById/','chieti.views.findProductById'),
    url(r'printPrice/','chieti.views.printPrice'),
    url(r'logOut/','chieti.views.logOut'),
    url(r'singInPop/','chieti.views.singInPop'),
    url(r'confirmOrder/','chieti.views.confirmOrder'),


    url(r'^$','chieti.views.home'),
	
)

