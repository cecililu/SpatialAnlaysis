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
        lng = float(request.GET.get('lng'))
        # print('bef float',lng)
        
        # lng=(float(lng))
        # print('after float',lng)
        buffer_distance = float(request.GET.get('buffer_distance'))
         
        # point = Point(lng, lat,srid=4326)
        
        
       
        p4326=Point(lng, lat, srid=4326)
        print('lat long sent',lng,lat)
        print('lat long got',p4326)
        ct = CoordTransform(SpatialReference(4326), SpatialReference(3857))
        p3857 = p4326.transform(ct, clone=True)
        buffer_polygon_3857 = p3857.buffer(buffer_distance/100000)
        buffer_polygon_4326 = p4326.buffer(buffer_distance/100000)
        
        print('Point transformned---->>>>>>',p4326)
      
        # buildings = PlanetOsmPolygon.objects.filter(
        # way__touches=buffer_polygon_4326,
        #                         building='yes')[:10]
    
        # print('ok')   
 
        query = """
  SELECT *
FROM planet_osm_polygon
WHERE ST_Intersects(
  way,
  ST_Transform(
    ST_MakeEnvelope(85.28460208092133, 27.606122394532917, 85.35535620512481, 27.69326664414035, 4326),
    3857
  )
) AND
 
  building = 'yes'  AND
  ST_DWithin(
    ST_Transform(
      ST_SetSRID(
        ST_Point(%s, %s),
        4326
      ),
      3857
    ),
    ST_Transform(way, 3857),
    %s
  )
LIMIT 10000;
"""
        with connection.cursor() as cursor:
           
            cursor.execute("EXPLAIN ANALYZE " + query, [p4326.x, p4326.y,buffer_distance])
            explain_result = cursor.fetchall()
            print("Query plan:")
            for plan in explain_result:
                print(plan)
            
            cursor.execute(query , [p4326.x, p4326.y,buffer_distance])
            rows = cursor.fetchall()

# Process the results
        buildings = [] 
        for row in rows:
            # Do something with each row
            way_wkb = row[-1]
            osm_id=row[0]
            amenities=row[2]
            way_geometry = GEOSGeometry(way_wkb) 
            way_geometryt= way_geometry.transform(4326, clone=True)
            buildings.append([way_geometryt,osm_id,amenities])
                
                
        
        features = []
        for building in buildings:
          
            geos_polygon = building[0]
            osm_id=building[1]
            # print('asdads',geos_polygon.geojson)
            feature = {
                "type": "Feature",
                "geometry":json.loads(geos_polygon.geojson),
                "properties": {"osm_id":osm_id,"amenities":building[2]}
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
      

# from rest_framework.response import Response
# from .models import  BuildingAttributeInformationModel
# from .sereializer import BuildingAttributeInformationSerializer

# class CreateBuildingAttributeInfo(APIView):
  
#     def post(self, request):
#         osm_id = request.data.get('osm_id')
#         hsn = request.data.get('house_metric_number')
        
#         print('Iam OSM ID---->',osm_id)
        
#         try:
#             building = PlanetOsmPolygon.objects.get(osm_id=osm_id)
#         except PlanetOsmPolygon.DoesNotExist:
#             return Response({'message': 'Building not found'}, status=404)
        
#         try: 
#            serializer = BuildingAttributeInformationSerializer(building=building,house_metric_number=hsn)
#            if serializer.is_valid():
#             #  serializer.validated_data['building'] = building
#              serializer.save()
#              return Response({'message': 'Building attribute information created successfully'}, status=201)
#         # else:
#         except:
#             return Response('Data could not be added check your data', status=400)


# add new building data

from .sereializer import *
from osgeo import ogr, osr


class BuildingdataPost(APIView):
  
    def post(self, request):
        data = request.data
        osm_id = data.get('osm_id')
        way = data.get('way')
        building=data.get('building')
        coords_str = way.split("((")[1].split("))")[0]
        coords = [c.strip().split(" ") for c in coords_str.split(",")]
        coords.append(coords[0])
        new_coords_str = ",".join([" ".join(c) for c in coords])
        output_wkt = f"POLYGON(({new_coords_str}))"
        print('cliet',output_wkt) 
        
        ogr_geometry = GEOSGeometry(output_wkt, srid=4326)
        ogr_geometry.transform(3857)
        print('--->',ogr_geometry)
        
        # building_attrs = data.get('building_attrs', {})
        building = PlanetOsmPolygon.objects.create(osm_id=osm_id, way=ogr_geometry, building=building)
        # building_attr_info = BuildingAttributeInformationModel.objects.create(building=building, **building_attrs)
        print('ok') 
        return Response({'message': 'Building data created successfully.'})