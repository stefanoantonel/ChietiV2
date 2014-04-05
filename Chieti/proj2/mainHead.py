from django.http import HttpResponse
from django.template import Context, Template

# Create your views here.
def head(request):
    fp = open('./proj2/templates/proj2/mainHead.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context())
    return HttpResponse(html)