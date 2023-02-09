from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
import osgeo.ogr

class BufferPolygonView(View):
    def get(self, request, *args, **kwargs):
        lat = float(request.GET.get('lat'))
        lon = float(request.GET.get('lon'))
        buffer_distance = float(request.GET.get('buffer_distance'))

        # Create a point using the lat/lon coordinates
        point = osgeo.ogr.Geometry(osgeo.ogr.wkbPoint)
        point.AddPoint(lon, lat)

        # Create a buffer polygon around the point
        buffer_polygon = point.Buffer(buffer_distance)

        # Convert the buffer polygon to JSON format
        polygon_json = buffer_polygon.ExportToJson()

        # Return the buffer polygon as a JSON response
        return JsonResponse({'polygon': polygon_json})