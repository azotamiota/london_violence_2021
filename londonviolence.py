import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import folium.plugins

# Load data
df1=pd.read_csv('D:\\inuse\\2021-01-city-of-london-street.csv')
df2=pd.read_csv('D:\\inuse\\2021-02-city-of-london-street.csv')
df3=pd.read_csv('D:\\inuse\\2021-03-city-of-london-street.csv')
df4=pd.read_csv('D:\\inuse\\2021-04-city-of-london-street.csv')
df5=pd.read_csv('D:\\inuse\\2021-05-city-of-london-street.csv')
df6=pd.read_csv('D:\\inuse\\2021-01-metropolitan-street.csv')
df7=pd.read_csv('D:\\inuse\\2021-02-metropolitan-street.csv')
df8=pd.read_csv('D:\\inuse\\2021-03-metropolitan-street.csv')
df9=pd.read_csv('D:\\inuse\\2021-04-metropolitan-street.csv')
df10=pd.read_csv('D:\\inuse\\2021-05-metropolitan-street.csv')

# Merge dataframes
fulldf = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=0)

# Clean data
fulldf=fulldf[fulldf['Crime type'] == 'Violence and sexual offences']
fulldf.reset_index(inplace=True)
fulldf=fulldf[fulldf['Longitude'].notna()]
fulldf_gdf=gpd.GeoDataFrame(fulldf, geometry=gpd.points_from_xy(fulldf['Longitude'], fulldf['Latitude']))

# Load London's borough map
london = gpd.read_file(gpd.datasets.get_path('London_Borough_Excluding_MHW'))

# Create background map
map = folium.Map(location=[51.51,-0.10], tiles='openstreetmap', zoom_start=10.5)

# Add London's borogh map to base map
folium.Choropleth(geo_data=london, fill_opacity=0).add_to(map)

# Add heatmap showing offences
folium.plugins.HeatMap(data=fulldf_gdf[['Latitude', 'Longitude']], radius=12,
                       name='Violence and sexual offences (2021)', min_opacity=0.4).add_to(map)

# Save html
map.save('londonviolence.html')

