# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:43:30 2020

@author: ASUS
"""

import pandas as pd
data = pd.read_csv("subset.csv")

Y = data['fraud_ind']
X = data.drop(['fraud_ind'],axis=1)

input_data = X.values.tolist()

train_x = input_data[0:100]
test_x = input_data[100:]

train_y = Y[0:100]
test_y = Y[100:]

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf.fit(train_x, train_y)

prediction = clf.predict(test_x)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(test_y, prediction)