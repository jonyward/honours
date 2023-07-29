from django.http import HttpResponse
from django.template import loader

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

# Create your views here.
