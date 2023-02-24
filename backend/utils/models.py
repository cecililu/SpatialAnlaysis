from django.contrib.gis.db import models
# Create your models here.

class PlanetOsmLine(models.Model):
    osm_id = models.BigIntegerField(primary_key=True,unique=True),
    access = models.TextField(blank=True, null=True)
    addr_housename = models.TextField(db_column='addr:housename', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housenumber = models.TextField(db_column='addr:housenumber', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_interpolation = models.TextField(db_column='addr:interpolation', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    admin_level = models.TextField(blank=True, null=True)
    aerialway = models.TextField(blank=True, null=True)
    aeroway = models.TextField(blank=True, null=True)
    amenity = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    barrier = models.TextField(blank=True, null=True)
    bicycle = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    bridge = models.TextField(blank=True, null=True)
    boundary = models.TextField(blank=True, null=True)
    building = models.TextField(blank=True, null=True)
    construction = models.TextField(blank=True, null=True)
    covered = models.TextField(blank=True, null=True)
    culvert = models.TextField(blank=True, null=True)
    cutting = models.TextField(blank=True, null=True)
    denomination = models.TextField(blank=True, null=True)
    disused = models.TextField(blank=True, null=True)
    embankment = models.TextField(blank=True, null=True)
    foot = models.TextField(blank=True, null=True)
    generator_source = models.TextField(db_column='generator:source', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    harbour = models.TextField(blank=True, null=True)
    highway = models.TextField(blank=True, null=True)
    historic = models.TextField(blank=True, null=True)
    horse = models.TextField(blank=True, null=True)
    intermittent = models.TextField(blank=True, null=True)
    junction = models.TextField(blank=True, null=True)
    landuse = models.TextField(blank=True, null=True)
    layer = models.TextField(blank=True, null=True)
    leisure = models.TextField(blank=True, null=True)
    lock = models.TextField(blank=True, null=True)
    man_made = models.TextField(blank=True, null=True)
    military = models.TextField(blank=True, null=True)
    motorcar = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    natural = models.TextField(blank=True, null=True)
    office = models.TextField(blank=True, null=True)
    oneway = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    power = models.TextField(blank=True, null=True)
    power_source = models.TextField(blank=True, null=True)
    public_transport = models.TextField(blank=True, null=True)
    railway = models.TextField(blank=True, null=True)
    ref = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)
    shop = models.TextField(blank=True, null=True)
    sport = models.TextField(blank=True, null=True)
    surface = models.TextField(blank=True, null=True)
    toll = models.TextField(blank=True, null=True)
    tourism = models.TextField(blank=True, null=True)
    tower_type = models.TextField(db_column='tower:type', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tracktype = models.TextField(blank=True, null=True)
    tunnel = models.TextField(blank=True, null=True)
    water = models.TextField(blank=True, null=True)
    waterway = models.TextField(blank=True, null=True)
    wetland = models.TextField(blank=True, null=True)
    width = models.TextField(blank=True, null=True)
    wood = models.TextField(blank=True, null=True)
    z_order = models.IntegerField(blank=True, null=True)
    way_area = models.FloatField(blank=True, null=True)
    way = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planet_osm_line'


class PlanetOsmPoint(models.Model):
    osm_id = models.BigIntegerField(blank=True, primary_key=True)
    access = models.TextField(blank=True, null=True)
    addr_housename = models.TextField(db_column='addr:housename', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housenumber = models.TextField(db_column='addr:housenumber', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_interpolation = models.TextField(db_column='addr:interpolation', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    admin_level = models.TextField(blank=True, null=True)
    aerialway = models.TextField(blank=True, null=True)
    aeroway = models.TextField(blank=True, null=True)
    amenity = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    barrier = models.TextField(blank=True, null=True)
    bicycle = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    bridge = models.TextField(blank=True, null=True)
    boundary = models.TextField(blank=True, null=True)
    building = models.TextField(blank=True, null=True)
    capital = models.TextField(blank=True, null=True)
    construction = models.TextField(blank=True, null=True)
    covered = models.TextField(blank=True, null=True)
    culvert = models.TextField(blank=True, null=True)
    cutting = models.TextField(blank=True, null=True)
    denomination = models.TextField(blank=True, null=True)
    disused = models.TextField(blank=True, null=True)
    ele = models.TextField(blank=True, null=True)
    embankment = models.TextField(blank=True, null=True)
    foot = models.TextField(blank=True, null=True)
    generator_source = models.TextField(db_column='generator:source', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    harbour = models.TextField(blank=True, null=True)
    highway = models.TextField(blank=True, null=True)
    historic = models.TextField(blank=True, null=True)
    horse = models.TextField(blank=True, null=True)
    intermittent = models.TextField(blank=True, null=True)
    junction = models.TextField(blank=True, null=True)
    landuse = models.TextField(blank=True, null=True)
    layer = models.TextField(blank=True, null=True)
    leisure = models.TextField(blank=True, null=True)
    lock = models.TextField(blank=True, null=True)
    man_made = models.TextField(blank=True, null=True)
    military = models.TextField(blank=True, null=True)
    motorcar = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    natural = models.TextField(blank=True, null=True)
    office = models.TextField(blank=True, null=True)
    oneway = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    poi = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    power = models.TextField(blank=True, null=True)
    power_source = models.TextField(blank=True, null=True)
    public_transport = models.TextField(blank=True, null=True)
    railway = models.TextField(blank=True, null=True)
    ref = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)
    shop = models.TextField(blank=True, null=True)
    sport = models.TextField(blank=True, null=True)
    surface = models.TextField(blank=True, null=True)
    toll = models.TextField(blank=True, null=True)
    tourism = models.TextField(blank=True, null=True)
    tower_type = models.TextField(db_column='tower:type', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tunnel = models.TextField(blank=True, null=True)
    water = models.TextField(blank=True, null=True)
    waterway = models.TextField(blank=True, null=True)
    wetland = models.TextField(blank=True, null=True)
    width = models.TextField(blank=True, null=True)
    wood = models.TextField(blank=True, null=True)
    z_order = models.IntegerField(blank=True, null=True)
    way = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planet_osm_point'


class PlanetOsmPolygon(models.Model):
    
    osm_id = models.BigIntegerField(blank=True,primary_key=True,unique=True)
    access = models.TextField(blank=True, null=True)
    addr_housename = models.TextField(db_column='addr:housename', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housenumber = models.TextField(db_column='addr:housenumber', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_interpolation = models.TextField(db_column='addr:interpolation', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    admin_level = models.TextField(blank=True, null=True)
    aerialway = models.TextField(blank=True, null=True)
    aeroway = models.TextField(blank=True, null=True)
    amenity = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    barrier = models.TextField(blank=True, null=True)
    bicycle = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    bridge = models.TextField(blank=True, null=True)
    boundary = models.TextField(blank=True, null=True)
    building = models.TextField(blank=True, null=True)
    construction = models.TextField(blank=True, null=True)
    covered = models.TextField(blank=True, null=True)
    culvert = models.TextField(blank=True, null=True)
    cutting = models.TextField(blank=True, null=True)
    denomination = models.TextField(blank=True, null=True)
    disused = models.TextField(blank=True, null=True)
    embankment = models.TextField(blank=True, null=True)
    foot = models.TextField(blank=True, null=True)
    generator_source = models.TextField(db_column='generator:source', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    harbour = models.TextField(blank=True, null=True)
    highway = models.TextField(blank=True, null=True)
    historic = models.TextField(blank=True, null=True)
    horse = models.TextField(blank=True, null=True)
    intermittent = models.TextField(blank=True, null=True)
    junction = models.TextField(blank=True, null=True)
    landuse = models.TextField(blank=True, null=True)
    layer = models.TextField(blank=True, null=True)
    leisure = models.TextField(blank=True, null=True)
    lock = models.TextField(blank=True, null=True)
    man_made = models.TextField(blank=True, null=True)
    military = models.TextField(blank=True, null=True)
    motorcar = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    natural = models.TextField(blank=True, null=True)
    office = models.TextField(blank=True, null=True)
    oneway = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    power = models.TextField(blank=True, null=True)
    power_source = models.TextField(blank=True, null=True)
    public_transport = models.TextField(blank=True, null=True)
    railway = models.TextField(blank=True, null=True)
    ref = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)
    shop = models.TextField(blank=True, null=True)
    sport = models.TextField(blank=True, null=True)
    surface = models.TextField(blank=True, null=True)
    toll = models.TextField(blank=True, null=True)
    tourism = models.TextField(blank=True, null=True)
    tower_type = models.TextField(db_column='tower:type', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tracktype = models.TextField(blank=True, null=True)
    tunnel = models.TextField(blank=True, null=True)
    water = models.TextField(blank=True, null=True)
    waterway = models.TextField(blank=True, null=True)
    wetland = models.TextField(blank=True, null=True)
    width = models.TextField(blank=True, null=True)
    wood = models.TextField(blank=True, null=True)
    z_order = models.IntegerField(blank=True, null=True)
    way_area = models.FloatField(blank=True, null=True)
    way = models.GeometryField(blank=True, null=True,srid=3857)

    class Meta:
        managed = False
        db_table = 'planet_osm_polygon'


class PlanetOsmRoads(models.Model):
    osm_id = models.BigIntegerField(primary_key=True)
    access = models.TextField(blank=True, null=True)
    addr_housename = models.TextField(db_column='addr:housename', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_housenumber = models.TextField(db_column='addr:housenumber', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_interpolation = models.TextField(db_column='addr:interpolation', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    admin_level = models.TextField(blank=True, null=True)
    aerialway = models.TextField(blank=True, null=True)
    aeroway = models.TextField(blank=True, null=True)
    amenity = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    barrier = models.TextField(blank=True, null=True)
    bicycle = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    bridge = models.TextField(blank=True, null=True)
    boundary = models.TextField(blank=True, null=True)
    building = models.TextField(blank=True, null=True)
    construction = models.TextField(blank=True, null=True)
    covered = models.TextField(blank=True, null=True)
    culvert = models.TextField(blank=True, null=True)
    cutting = models.TextField(blank=True, null=True)
    denomination = models.TextField(blank=True, null=True)
    disused = models.TextField(blank=True, null=True)
    embankment = models.TextField(blank=True, null=True)
    foot = models.TextField(blank=True, null=True)
    generator_source = models.TextField(db_column='generator:source', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    harbour = models.TextField(blank=True, null=True)
    highway = models.TextField(blank=True, null=True)
    historic = models.TextField(blank=True, null=True)
    horse = models.TextField(blank=True, null=True)
    intermittent = models.TextField(blank=True, null=True)
    junction = models.TextField(blank=True, null=True)
    landuse = models.TextField(blank=True, null=True)
    layer = models.TextField(blank=True, null=True)
    leisure = models.TextField(blank=True, null=True)
    lock = models.TextField(blank=True, null=True)
    man_made = models.TextField(blank=True, null=True)
    military = models.TextField(blank=True, null=True)
    motorcar = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    natural = models.TextField(blank=True, null=True)
    office = models.TextField(blank=True, null=True)
    oneway = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    power = models.TextField(blank=True, null=True)
    power_source = models.TextField(blank=True, null=True)
    public_transport = models.TextField(blank=True, null=True)
    railway = models.TextField(blank=True, null=True)
    ref = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)
    shop = models.TextField(blank=True, null=True)
    sport = models.TextField(blank=True, null=True)
    surface = models.TextField(blank=True, null=True)
    toll = models.TextField(blank=True, null=True)
    tourism = models.TextField(blank=True, null=True)
    tower_type = models.TextField(db_column='tower:type', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tracktype = models.TextField(blank=True, null=True)
    tunnel = models.TextField(blank=True, null=True)
    water = models.TextField(blank=True, null=True)
    waterway = models.TextField(blank=True, null=True)
    wetland = models.TextField(blank=True, null=True)
    width = models.TextField(blank=True, null=True)
    wood = models.TextField(blank=True, null=True)
    z_order = models.IntegerField(blank=True, null=True)
    way_area = models.FloatField(blank=True, null=True)
    way = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planet_osm_roads'

# class BuildingData(models.Model):
#     osmdata=models.OneToOneField(PlanetOsmPolygon,on_delete=models.CASCADE,to_field='osm_id')
#     address=models.CharField(max_length=100,blank=True,null=True)
#     phone1 = models.CharField(max_length=20,blank=True,null=True)
#     phone2 = models.CharField(max_length=20,blank=True,null=True)
#     people=models.IntegerField(blank=True,null=True)   

# class BuildingAttributeInformationModels(models.Model):
#     house_metric_number = models.CharField(primary_key=True, max_length=50)
#     # Add any other fields for the BuildingAttributeInformationModel model here
#     building = models.ForeignKey(PlanetOsmPolygon, on_delete=models.CASCADE,to_field='osm_id',null=True)
#     address=models.CharField(max_length=100,blank=True,null=True)
#     phone1 = models.CharField(max_length=20,blank=True,null=True)
#     phone2 = models.CharField(max_length=20,blank=True,null=True)

# class Data(models.Model):
#     house_metric_number = models.CharField(primary_key=True, max_length=100)
#     address = models.CharField(max_length=100, blank=True, null=True)
#     phone1 = models.CharField(max_length=20, blank=True, null=True)
#     phone2 = models.CharField(max_length=20, blank=True, null=True)
#     building_id = models.OneToOneField(
#         PlanetOsmPolygon,
#         blank=True,
#         null=True,
#         on_delete=models.CASCADE,
#         to_field='osm_id' # specify the name of the column to use as the reference
#     )
class Data(models.Model):
    house_metric_number = models.CharField(primary_key=True, max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    building = models.ForeignKey('PlanetOsmPolygon', models.DO_NOTHING, blank=True, null=True)
    people = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'

