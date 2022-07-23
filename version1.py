import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import random as rd
import matplotlib.pyplot as plt
from math import sqrt
import csv
import numpy
from sklearn.decomposition import PCA
from mpl_toolkits import mplot3d
#Import required module
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# loading  the modulus of impedance datafile into a data frame.
df = pd.read_csv('C:/Users/pasiv/Desktop/impedance.csv', encoding='unicode_escape')
df.drop(columns = ["Pt #", "IERange","labels"], inplace = True)
# print(df)

#Scaling the data between 0 and 1
scaler = MinMaxScaler()
scaler.fit(df[['Zmod(in ohms)']])
df['Zmod(in ohms)'] = scaler.transform(df[['Zmod(in ohms)']])
scaler.fit(df[['Time (sec)']])
df['Time (sec)'] = scaler.transform(df[['Time (sec)']])
plt.scatter(df['Time (sec)'],df['Zmod(in ohms)'])
print(df)

#Principal Component Analysis- following code shows the variance with respect to the Principal Components
pca = PCA()
df_pca = pd.DataFrame(pca.fit_transform(df_scaled))
print(df_pca)
import matplotlib.pyplot as plt
pd.DataFrame(pca.explained_variance_ratio_).plot.bar()
plt.legend('')
plt.xlabel('Principal Components')
plt.ylabel('Explained Varience');
# plt.show()

from sklearn.decomposition import PCA
pca=PCA(n_components=2)
print(pca.fit(df_pca))
x_pca=pca.transform(df_pca)
print('Dimension of scaled data',df.shape)
print('Scaled data is ',df_pca)
print('The dimensions after reduction is',x_pca.shape)
print('The data after application of PCA is',x_pca)
plt.figure(figsize=(8,6))
plt.scatter(['Time (sec)'],['Zmod(in ohms)'], color = "green")
plt.xlabel('First principle component')
plt.ylabel('Second principle component')
plt.show()


#defining clusters
km = KMeans(n_clusters=4)
y_predicted = km.fit_predict(df[['Time (sec)','Zmod(in ohms)']])
print(y_predicted)

df['cluster']=y_predicted
print(df.tail(10))
print(km.cluster_centers_)

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1['Time (sec)'],df1['Zmod(in ohms)'],color='blue')
plt.scatter(df2['Time (sec)'],df2['Zmod(in ohms)'],color='green')
plt.scatter(df3['Time (sec)'],df3['Zmod(in ohms)'],color='black')
plt.scatter(df4['Time (sec)'],df4['Zmod(in ohms)'],color='red')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
print(df1)
plt.title('K means clustering ')
plt.xlabel('Time')
plt.ylabel('Modulus of impedance(in ohms)')
plt.legend()
plt.show()

#displaying elbow plot to verify if the selected no of clusters were correct.
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['Time (sec)','Zmod(in ohms)']])
    sse.append(km.inertia_)
plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)    
plt.show()





