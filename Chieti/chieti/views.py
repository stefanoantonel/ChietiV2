from django.shortcuts import render
from django.http import request, HttpResponse

# Create your views here.
def java_script(request):
    filename = request.path.strip("/")
    data = open(filename, "rb").read()
    return HttpResponse(data, mimetype="application/x-javascript")

def add(request):
    print "en views"
    pass
