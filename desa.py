import geopandas as gpd
import matplotlib.pyplot as plt
import os

input_folder = r'E:\Project\GH\batas\geojson'
output_folder = r'E:\Project\GH\batas\geojson\hasil'

daftar_file = [
    '35.13.13.2001.geojson', '35.13.13.2002.geojson', '35.13.13.2003.geojson', '35.13.13.2004.geojson',
    '35.13.13.2005.geojson', '35.13.13.2006.geojson', '35.13.13.2007.geojson', '35.13.13.2008.geojson',
    '35.13.13.2009.geojson', '35.13.13.2010.geojson', '35.13.13.2011.geojson', '35.13.13.2012.geojson',
    '35.13.13.2013.geojson', '35.13.13.2014.geojson', '35.13.13.2015.geojson', '35.13.13.2016.geojson',
    '35.13.13.2017.geojson'
]

for file in daftar_file :
    gdf = gpd.read_file(os.path.join(input_folder, file))

    # Menggabungkan geometri
    boundary = gdf.unary_union
    boundary_gdf = gpd.GeoDataFrame(geometry=[boundary], crs=gdf.crs)

    # Menyimpan hasil ke file GeoJSON
    output_file_name = f'batas_{os.path.splitext(file)[0]}.geojson'
    boundary_gdf.to_file(os.path.join(output_folder, output_file_name), driver='GeoJSON')

    # Membaca dan memplot hasil
    boundary_check = gpd.read_file(os.path.join(output_folder, output_file_name))
    boundary_check.plot()
    plt.title(output_file_name)
    plt.show()
