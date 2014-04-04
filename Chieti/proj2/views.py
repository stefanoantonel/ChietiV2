from django.shortcuts import render

# Create your views here.
def java_script(request):
    filename = request.path.strip("/")
    data = open(filename, "rb").read()
    return HttpResponse(data, mimetype="application/x-javascript")
