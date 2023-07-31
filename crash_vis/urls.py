from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about', views.about, name='about'),
    path('markermap', views.markermap, name='markermap'),
    path('heatmap', views.heatmap, name='heatmap'),
]