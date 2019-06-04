import pandas as pd

#Read CSV file
data = pd.read_csv('Oullins/14.csv')
#Exclude extreme values
df = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
d14 = df.groupby(['type_local']).mean()
print(d14)


#Read CSV file
data = pd.read_csv('Oullins/15.csv')
#Exclude extreme values
df = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
d15 = df.groupby(['type_local']).mean()
print(d15)

#Read CSV file
data = pd.read_csv('Oullins/16.csv')
#Exclude extreme values
df = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
d16 = df.groupby(['type_local']).mean()
print(d16)

#Read CSV file
data = pd.read_csv('Oullins/17.csv')
#Exclude extreme values
df = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
d17 = df.groupby(['type_local']).mean()
print(d17)

#Read CSV file
data = pd.read_csv('Oullins/18.csv')
#Exclude extreme values
df = data.loc[(data['prix_m2'] >= 1000) & (data['prix_m2'] <= 10000),:]
#Calculate mean according to local type
d18 = df.groupby(['type_local']).mean()
print(d18)