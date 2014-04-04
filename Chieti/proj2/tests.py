from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
# Create your tests here.
def index(request):

	p = request.GET.get('p')
	#if p is not None:
	#    return HttpResponse(p)
	#else:
	#    return HttpResponse("No hay p ")
	
	#from django.template import Context, Template
	#t = Template("Mi nombre es {{ nombre }}.")
	#c = Context({"nombre": p})
	#return HttpResponse(t.render(c))

	from django.template import Context, Template
	t = Template("Mi nombre es {{ nombre }}.")
	c = Context({"nombre": p})
	#html = open("/1.html")
	#return HttpResponse(html)
	
	#fp = open('D:\Programas Facultad\Diego G\workspace\github\ChiettiRepo\Chieti\proj2\templates\proj2\1.html')
	fp = open('./proj2/templates/proj2/1.html')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context())
	return HttpResponse(html)
	
	
