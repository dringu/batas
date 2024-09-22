import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file(r'E:\Project\GH\batas\geojson\35.13.geojson')

boundary = gdf.unary_union
boundary_gdf = gpd.GeoDataFrame(geometry=[boundary], crs=gdf.crs)
boundary_gdf.to_file(r'E:\Project\GH\batas\geojson\hasil\batas_probolinggo.geojson', driver='GeoJSON')

boundary_check = gpd.read_file(r'E:\Project\GH\batas\geojson\hasil\batas_probolinggo.geojson')

boundary_check.plot()
plt.show()