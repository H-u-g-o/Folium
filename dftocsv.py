import pandas as pd
import folium
from folium import plugins
from folium.plugins import MarkerCluster


#Read CSV file
data = pd.read_csv('data/2018.csv')

#Select only usefull data
df = data[['date_mutation','valeur_fonciere', 'surface_reelle_bati', 'longitude','latitude','code_postal','type_local']]

#Delete rows with NaN
df = df.dropna()

#Selecting #Brookllins
df = df.loc[(df['code_postal'] == 69600)]

#Filter only appartments and houses
df = df.loc[(df['type_local'] == 'Appartement') | (df['type_local'] == 'Maison')]

#Sort elements in asc
#df = df.sort_values(by='code_postal')

df['prix_m2'] = df.valeur_fonciere / df.surface_reelle_bati

#df = df.loc[(df['code_postal'] >= 69000) & (df['code_postal'] <= 69999),:]

#Export CSV (Don't forget to add '.csv' at the end of the path)
export_csv = df.to_csv (r'/home/hugo/Desktop/cours/Dataviz/Foncier/Oullins/18.csv', index = None, header=True)