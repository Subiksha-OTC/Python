# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:25:01 2020

@author: Subiksha Godfrey
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
type(iris) 

#Reading the dataset
print (iris.data)
iris.data.shape
# print the names of the four features
print (iris.feature_names)
# print the encoding scheme for species; 0 = Setosa , 1=Versicolor, 2= virginica
print (iris.target_names)
type('iris.data')
type('iris.target')
featuresAll=[]
features = iris.data[: , [0,1,2,3]]
features.shape
for observation in features:
    featuresAll.append([observation[0] + observation[1] + observation[2] + observation[3]])
print (featuresAll)
# Plotting the Scatter plot
# Extract the values for targets
targets = iris.target
targets.reshape(targets.shape[0],-1)
targets.shape

plt.scatter(featuresAll, targets, color='red', alpha =1.0)
plt.rcParams['figure.figsize'] = [10,8]
plt.title('Iris Dataset scatter Plot')
plt.xlabel('Features')
plt.ylabel('Targets')

plt.scatter(featuresAll, targets, color='red', alpha =1.0)
plt.rcParams['figure.figsize'] = [10,8]
plt.title('Iris Dataset scatter Plot')
plt.xlabel('Features')
plt.ylabel('Targets')
from sklearn.decomposition import PCA  # 1. Choose the model class
model = PCA(n_components=2)  # 2. Instantiate the model with hyperparameters 
# =============================================================================
# model.fit(X3) 
# X_2D = model.transform(X3)
# 
# =============================================================================
dataset = pd.read_csv("iris.csv", header = None, names = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width','variety'])
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values
#label encoding the Target values
from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

#Reducing the dimensions for 3D
from sklearn.decomposition import PCA
pca = PCA(n_components=3)
X = pca.fit_transform(X)


#Visualising the 3D chart
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(1, figsize=(4, 3))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()

# Reorder the labels to have colors matching the cluster results
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.spectral, edgecolor='k')
plt.show()
