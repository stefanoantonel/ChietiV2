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

	from django.template import Context, Template

	#html = open("/1.html")
	#return HttpResponse(html)
	
	#fp = open('D:\Programas Facultad\Diego G\workspace\github\ChiettiRepo\Chieti\chieti\templates\chieti\1.html')
	fp = open('./chieti/templates/chieti/1.html')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context())
	return HttpResponse(html)
	
