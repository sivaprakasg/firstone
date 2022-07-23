import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import random as rd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import csv
#Import required module
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
        
# loading  the modulus of impedance datafile into a data frame.
df = pd.read_csv("C:/Users/pasiv/Desktop/test.csv")
# print(df.head(10))
# print()

#scaling data between limits 0 and 1
# scaler = MinMaxScaler()
# scaler.fit(df[['Zmod(in ohms)']])
# df['Zmod(in ohms)'] = scaler.transform(df[['Zmod(in ohms)']])
# scaler.fit(df[['Time (sec)']])
# df['Time (sec)'] = scaler.transform(df[['Time (sec)']])
# plt.scatter(df['Time (sec)'],df['Zmod(in ohms)'])

df.fillna(0, inplace = True)
x = df.iloc[:,1:]

#pca implementation
pca = PCA(2)
data = pca.fit_transform(x)
plt.figure(figsize=(10,10))
var = np.round(pca.explained_variance_ratio_*100, decimals = 1)
lbls = [str(x) for x in range(1,len(var)+1)]
plt.bar(x=range(1,len(var)+1), height = var, tick_label = lbls)
plt.show()

#defining clusters
km = KMeans(n_clusters=4)
y_predicted = km.fit_predict(df[['Time (sec)','Zmod(in ohms)']])
# print(y_predicted)

df['cluster']=y_predicted
# print(df.head())
# print(km.cluster_centers_)

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
df4 = df[df.cluster==3]
plt.scatter(df1['Time (sec)'],df1['Zmod(in ohms)'],color='green')
plt.scatter(df2['Time (sec)'],df2['Zmod(in ohms)'],color='red')
plt.scatter(df3['Time (sec)'],df3['Zmod(in ohms)'],color='black')
plt.scatter(df4['Time (sec)'],df4['Zmod(in ohms)'],color='blue')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
print(df2)


plt.xlabel('Time')
plt.ylabel('modulus of impedance')
plt.legend()


wcss = []
for i in range(1,11):
   model = KMeans(n_clusters = i, init = "k-means++")
   model.fit(df)
   wcss.append(model.inertia_)
plt.figure(figsize=(10,10))
plt.plot(range(1,11), wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()