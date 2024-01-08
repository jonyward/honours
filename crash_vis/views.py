from django.shortcuts import render
import folium
from folium.plugins import FastMarkerCluster
from crash_vis.models import Crashes

def main(request):
    context = {}
    return render(request, 'main.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def markermap(request):
    context = {}
    return render(request, 'markermap.html', context)

def heatmap(request):
    context = {}
    return render(request, 'heatmap.html', context)

def testing(request):
    crashes = Crashes.objects.all()

    map = folium.Map(location=[55.5, -1.54], zoom_start=5)

    latitudes = [crash.Latitude for crash in crashes]
    longitudes = [crash.Longitude for crash in crashes]

    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(map)

    context = {'map': map._repr_html_()}
    return render(request, 'testing.html', context)

# Create your views here.
