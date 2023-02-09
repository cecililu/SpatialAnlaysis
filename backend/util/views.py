from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Polygon
from django.contrib.gis.measure import D
from django.http import JsonResponse
from django.views import View
import json
class BufferPolygonView(View):
    def get(self, request, *args, **kwargs):
        lat = float(request.GET.get('lat'))
        lon = float(request.GET.get('lon'))
        buffer_distance = float(request.GET.get('buffer_distance'))
        point = Point(lon, lat, srid=4326)
        buffer_polygon = point.buffer(buffer_distance/100000)

        # convert the buffer polygon to a geojson-compatible dictionary
        polygon_geojson = {
            'type': 'Feature',
            'geometry': json.loads(buffer_polygon.geojson),
            'properties': {
                'point': [lon, lat],
                'buffer_distance': buffer_distance,
            }
        }

        return JsonResponse(polygon_geojson)