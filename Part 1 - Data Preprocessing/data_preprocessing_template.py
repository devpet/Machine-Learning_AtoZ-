# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 17:34:35 2017

@author: pet56
"""
# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the data set
dataset = pd.read_csv('D:\Machine Learning A-Z Template Folder\Part 1 - Data Preprocessing\Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values
                
# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:, 1:3])