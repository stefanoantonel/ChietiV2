from django.test import TestCase
from django.http import request, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.template import Context, Template
# Create your tests here.
def index(request):

    
    fp = open('/chieti/homePage.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context())
    return HttpResponse(html)

    
    
