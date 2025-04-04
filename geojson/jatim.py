import geopandas as gpd
import pandas as pd
import os

# Mapping kode wilayah ke nama sesuai dengan dataset PDRB
kode_wilayah_mapping = {
    "35.01": "Pacitan",
    "35.02": "Ponorogo",
    "35.03": "Trenggalek",
    "35.04": "Tulungagung",
    "35.05": "Blitar",
    "35.06": "Kediri",
    "35.07": "Malang",
    "35.08": "Lumajang",
    "35.09": "Jember",
    "35.10": "Banyuwangi",
    "35.11": "Bondowoso",
    "35.12": "Situbondo",
    "35.13": "Probolinggo",
    "35.14": "Pasuruan",
    "35.15": "Sidoarjo",
    "35.16": "Mojokerto",
    "35.17": "Jombang",
    "35.18": "Nganjuk",
    "35.19": "Madiun",
    "35.20": "Magetan",
    "35.21": "Ngawi",
    "35.22": "Bojonegoro",
    "35.23": "Tuban",
    "35.24": "Lamongan",
    "35.25": "Gresik",
    "35.26": "Bangkalan",
    "35.27": "Sampang",
    "35.28": "Pamekasan",
    "35.29": "Sumenep",
    "35.71": "Kota Kediri",
    "35.72": "Kota Blitar",
    "35.73": "Kota Malang",
    "35.74": "Kota Probolinggo",
    "35.75": "Kota Pasuruan",
    "35.76": "Kota Mojokerto",
    "35.77": "Kota Madiun",
    "35.78": "Kota Surabaya",
    "35.79": "Kota Batu"
}

# Folder penyimpanan GeoJSON
geojson_folder = r"D:\git\pdrb\data"

# Load semua file GeoJSON
geojson_files = [os.path.join(geojson_folder, f) for f in os.listdir(geojson_folder) if f.endswith(".geojson")]

# Inisialisasi GeoDataFrame kosong untuk gabung semua wilayah
gdf_all = gpd.GeoDataFrame()

# Loop untuk membaca dan menyesuaikan nama kabupaten/kota
for file in geojson_files:
    kode_wilayah = os.path.basename(file).replace(".geojson", "")  # Ambil kode dari nama file
    if kode_wilayah in kode_wilayah_mapping:
        gdf = gpd.read_file(file)

        # Pastikan kolom 'name' ada di GeoJSON
        if 'name' not in gdf.columns:
            print(f"Kolom 'name' tidak ditemukan di {file}")
            continue

        # Konversi ke CRS WGS 84 untuk mencegah error
        gdf = gdf.to_crs("EPSG:4326")

        # Tambahkan nama wilayah yang sudah dinormalisasi
        gdf['Nama_Normalized'] = kode_wilayah_mapping[kode_wilayah]

        # Gabungkan dengan GeoDataFrame utama
        gdf_all = pd.concat([gdf_all, gdf], ignore_index=True)

# Simpan hasil gabungan ke file baru
output_geojson = r"E:\Project\GH\batas\geojson\hasil.geojson"
gdf_all.to_file(output_geojson, driver="GeoJSON")

print(f"Gabungan semua wilayah disimpan di: {output_geojson}")