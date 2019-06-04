import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Read CSV file
data = pd.read_csv('Oullins/14.csv')
#Exclude extreme values
d14 = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
d14 = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
#Appart
d14a =  d14.loc[d14['type_local']=="Appartement"]
d14a = d14a['prix_m2'].mean()
#Maison
d14m =  d14.loc[d14['type_local']=="Maison"]
d14m = d14m['prix_m2'].mean()


#Read CSV file
data = pd.read_csv('Oullins/15.csv')
#Exclude extreme values
d15 = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
d15 = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
#Appart
d15a =  d15.loc[d15['type_local']=="Appartement"]
d15a = d15a['prix_m2'].mean()
#Maison
d15m =  d15.loc[d15['type_local']=="Maison"]
d15m = d15m['prix_m2'].mean()

#Read CSV file
data = pd.read_csv('Oullins/16.csv')
#Exclude extreme values
d16 = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
d16 = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
#Appart
d16a =  d16.loc[d16['type_local']=="Appartement"]
d16a = d16a['prix_m2'].mean()
#Maison
d16m =  d16.loc[d16['type_local']=="Maison"]
d16m = d16m['prix_m2'].mean()

#Read CSV file
data = pd.read_csv('Oullins/17.csv')
#Exclude extreme values
d17 = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
#Appart
d17a =  d17.loc[d17['type_local']=="Appartement"]
d17a = d17a['prix_m2'].mean()
#Maison
d17m =  d17.loc[d17['type_local']=="Maison"]
d17m = d17m['prix_m2'].mean()

#Read CSV file
data = pd.read_csv('Oullins/18.csv')
#Exclude extreme values
d18 = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
#Appart
d18a =  d18.loc[d18['type_local']=="Appartement"]
d18a = d18a['prix_m2'].mean()
#Maison
d18m =  d18.loc[d18['type_local']=="Maison"]
d18m = d18m['prix_m2'].mean()

prix_m = (d14m,d15m,d16m,d17m,d18m)
prix_a = (d14a,d15a,d16a,d17a,d18a)

