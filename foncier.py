import csv
import pandas as pd
import folium
from folium import plugins
from folium.plugins import HeatMap



#Print column name
#for col in data.columns:
#    print(col)

#print data Types
#print(data.dtypes)

#Get number of Nan per Index
#print(df1.isna().sum())

#Get number of null per Index
#print((df1.isnull().sum() / len(df1))*100)

#change datatype to int
#data.code_postal = data.code_postal.astype(int)

#Read CSV file
data = pd.read_csv('data.csv')

locations = data[['latitude', 'longitude']]
locationlist = locations.values.tolist()

price = data['prix_m2']
price = price.values.tolist()

#Clear datatype and get separated time values
#data.date_mutation = pd.to_datetime(data.date_mutation, format='%Y-%m-%d')
#data['month'] = data.date_mutation.apply(lambda x: x.month)
#data['week'] = data.date_mutation.apply(lambda x: x.week)
#data['day'] = data.date_mutation.apply(lambda x: x.day)


# def generateBaseMap(default_location=[45.7372756, 4.8175837], default_zoom_start=12):
#      base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
#      return base_map

# base_map = generateBaseMap()

# HeatMapWithTime(locationlist).add_to(base_map)

# base_map.save('L.html')

#HeatMap

def generateBaseMap(default_location=[45.7372756, 4.8175837], default_zoom_start=12):
     base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
     return base_map
base_map = generateBaseMap()
HeatMap(data=data[['latitude', 'longitude']], gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'orange', 0.8: 'yellow', 1: 'red'}, radius=15, max_zoom=18).add_to(base_map)

base_map.save('M.html')

###Marker Cluster

# map2 = folium.Map(location=[45.7372756, 4.8175837], tiles='CartoDB dark_matter', zoom_start=11)

# marker_cluster = folium.plugins.MarkerCluster().add_to(map2)

# for point in range(0, len(locationlist)):
#     folium.Marker(locationlist[point], popup=price[point]).add_to(marker_cluster)
# map2.save('carte4.html')

