import csv
import pandas as pd
import folium
from folium import plugins
from folium.plugins import MarkerCluster


#Read CSV file
data = pd.read_csv('data.csv')



#Print column name
#for col in data.columns:
#    print(col)

#print data Types
#print(data.dtypes)

#Select only usefull data
df1 = data[['valeur_fonciere', 'surface_reelle_bati', 'longitude','latitude','code_postal','type_local']]

#Get number of Nan per Index
#print(df1.isna().sum())

#Get number of null per Index
#print((df1.isnull().sum() / len(df1))*100)

#Delete rows with NaN
df1 = df1.dropna()

#change datatype to int
#data.code_postal = data.code_postal.astype(int)

#Filter only appartments
df1 = df1.loc[df1['type_local']=="Appartement",:]

#Sort elements in asc
df1 = df1.sort_values(by='code_postal')

df1['prix_m2'] = df1.valeur_fonciere / df1.surface_reelle_bati
df1['prix_m2'] = df1['prix_m2'].round(1)

df1 = df1.loc[(df1['code_postal'] >= 69000) & (df1['code_postal'] <= 69001),:]


locations = df1[['latitude', 'longitude']]
locationlist = locations.values.tolist()

price = df1['prix_m2']
price = price.values.tolist()

# map = folium.Map(location=[45.7372756, 4.8175837], zoom_start=12)
# for point in range(0, len(locationlist)):
#       folium.Marker(locationlist[point], popup=price[point]).add_to(map)

# map.save('carte.html')

map2 = folium.Map(location=[45.7372756, 4.8175837], tiles='CartoDB dark_matter', zoom_start=11)

marker_cluster = folium.plugins.MarkerCluster().add_to(map2)

for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], popup=price[point]).add_to(marker_cluster)
map2.save('carte2.html')

