from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos import fromstr
from django.contrib.gis.geos import GEOSGeometry
from .models import PlanetOsmPolygon

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.contrib.gis.gdal import SpatialReference, CoordTransform
from django.db import connection


class BufferPolygonIntersectionView(APIView):
    def get(self, request):
        print('gettin buildings.... wait')
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lon'))
        buffer_distance = float(request.GET.get('buffer_distance'))
         
        # point = Point(lng, lat,srid=4326)
        
        
       
        p4326=Point(lng, lat, srid=4326)
        print('Point transformned',p4326)
        ct = CoordTransform(SpatialReference(4326), SpatialReference(3857))
        p3857 = p4326.transform(ct, clone=True)
        buffer_polygon_3857 = p3857.buffer(buffer_distance/100000)
        buffer_polygon_4326 = p4326.buffer(buffer_distance/100000)
        
        print('Point transformned',p3857)
      
        # buildings = PlanetOsmPolygon.objects.filter(
        # way__touches=buffer_polygon_4326,
        #                         building='yes')[:10]
    
        # print('ok')   
 

        query = """
    SELECT *
    FROM planet_osm_polygon
    WHERE ST_DWithin(
      ST_Transform(
        ST_SetSRID(
          ST_Point(%s, %s),
          4326
        ),
        3857
      ),
      ST_Transform(way, 3857),
      200
    ) AND admin_level is NULL AND building='yes'
    LIMIT 1000;
"""
        with connection.cursor() as cursor:
            cursor.execute(query, [p4326.x, p4326.y])

        # Process the results
            buildings=[] 
            for row in cursor.fetchall():
                # Do something with each row
                way_wkb = row[-1]
                way_geometry = GEOSGeometry(way_wkb) 
                buildings.append(way_geometry) 
        
        
        
        print(buildings,'runned')
        features = []
        for building in buildings:
            # print(building.way,'assasas')
            geos_polygon = building
            # geometry = GEOSGeometry(goes_polygon).json
            feature = {
                "type": "Feature",
                "geometry":json.loads(geos_polygon.geojson),
            
                "properties": {}
            }
            features.append(feature)
        
        feature_collection = {
            "type": "FeatureCollection",
            "features": features
        }
       
        return Response(feature_collection)
    
    
    
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