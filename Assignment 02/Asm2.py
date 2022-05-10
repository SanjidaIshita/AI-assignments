import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

data = pd.read_csv('worldcupplayers.csv')
data.head()

X = data[["age","caps"]]

plt.scatter(X["caps"],X["age"],c='black')
plt.xlabel('PalyerCap')
plt.ylabel('Player Age (In Years)')
#plt.show()

K=3

Centroids = (X.sample(n=K))
plt.scatter(X["caps"],X["age"],c='black')
plt.scatter(Centroids["caps"],Centroids["age"],c='red')
plt.xlabel('PalyerCap')
plt.ylabel('Player Age (In Years)')
#plt.show()

diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["caps"]-row_d["caps"])**2
            d2=(row_c["age"]-row_d["age"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1
    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Player"]=C
    Centroids_new = X.groupby(["Player"]).mean()[["age","caps"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['age'] - Centroids['age']).sum() + (Centroids_new['caps'] - Centroids['caps']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Player"]).mean()[["age","caps"]]
color = ['blue', 'green', 'cyan']
for k in range(K):
    data = X[X["Player"] == k + 1]
    plt.scatter(data["caps"], data["age"],c=color[k])
plt.scatter(Centroids["caps"], Centroids["age"],c='red')
plt.xlabel('Cap of Player')
plt.ylabel('Player Age (In Years)')
plt.show()
