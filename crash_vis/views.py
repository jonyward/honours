from django.http import HttpResponse
from django.template import loader

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def markermap(request):
    template = loader.get_template('markermap.html')
    return HttpResponse(template.render())

def heatmap(request):
    template = loader.get_template('heatmap.html')
    return HttpResponse(template.render())

# Create your views here.
