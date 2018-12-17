from shapely.geometry import Point
from geopandas import GeoDataFrame
from fiona.crs import from_epsg


# City of PHL Proj4 CRS
# http://spatialreference.org/ref/esri/nad-1983-stateplane-pennsylvania-south-fips-3702-feet/proj4/
PHL_CRS = '+proj=lcc +lat_1=39.93333333333333 +lat_2=40.96666666666667 +lat_0=39.33333333333334 +lon_0=-77.75 +x_0=600000.0000000001 +y_0=0 +ellps=GRS80 +datum=NAD83 +to_meter=0.3048006096012192 +no_defs' 

def create_point_geometry(df, x_col, y_col):
    geometry = [Point(xy) for xy in zip(df[x_col], df[y_col])]
    return geometry

def reproject_gdf(gdf, start_crs, end_crs):
    gdf.crs = from_epsg(start_crs)
    gdf = gdf.to_crs(end_crs)
    return gdf