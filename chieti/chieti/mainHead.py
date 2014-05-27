from django.http import HttpResponse
from django.template import Context, Template

# Create your views here.
def index(request):
    fp = open('./chieti/templates/chieti/mainHead.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context())
    return HttpResponse(html)
