from django.shortcuts import render
import folium
from folium.plugins import FastMarkerCluster, HeatMap, Fullscreen, MiniMap
from crash_vis.models import Crashes

def main(request):
    context = {}
    return render(request, 'main.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def markermap(request):
    crashes = Crashes.objects.all()

    map = folium.Map(location=[55.5, -1.54], zoom_start=5)

    latitudes = [crash.Latitude for crash in crashes]
    longitudes = [crash.Longitude for crash in crashes]

    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(map)
    Fullscreen(position='topleft', title='FULL SCREEN ON', title_cancel='FULL SCREEN OFF',force_separate_button=True).add_to(map)
    MiniMap().add_to(map)

    context = {'markermap': map._repr_html_()}
    return render(request, 'markermap.html', context)

def heatmap(request):
    crashes = Crashes.objects.all()

    map = folium.Map(location=[55.5, -1.54], zoom_start=5)

    latitudes = [crash.Latitude for crash in crashes]
    longitudes = [crash.Longitude for crash in crashes]

    HeatMap(data=list(zip(latitudes, longitudes))).add_to(map)
    Fullscreen(position='topleft', title='FULL SCREEN ON', title_cancel='FULL SCREEN OFF',force_separate_button=True).add_to(map)
    MiniMap().add_to(map)

    context = {'heatmap': map._repr_html_()}
    return render(request, 'heatmap.html', context)

#Views responsible for what templates are rendered, and map functionality
