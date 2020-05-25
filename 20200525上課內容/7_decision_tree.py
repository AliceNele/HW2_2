# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:14:31 2020

@author: CJ
"""


import pandas as pd
data = pd.read_csv("subset.csv")

Y = data['fraud_ind']
X = data.drop(['fraud_ind'],axis=1)

ecfg = pd.get_dummies(X.ecfg)
flbmk = pd.get_dummies(X.flbmk)
flg_3dsmk = pd.get_dummies(X.flg_3dsmk)
insfg = pd.get_dummies(X.insfg)
ovrlt = pd.get_dummies(X.ovrlt)

X = X.drop(['flbmk'],axis=1)
dummy_ecfg = ecfg["Y"].tolist()
dummy_flg_3dsmk = flg_3dsmk["Y"].tolist()
dummy_insfg = insfg["Y"].tolist()
dummy_ovrlt = ovrlt["Y"].tolist()

X['ecfg'] = dummy_ecfg
X['flg_3dsmk'] = dummy_flg_3dsmk
X['insfg'] = dummy_insfg
X['ovrlt'] = dummy_ovrlt

input_data = X.values.tolist()

from sklearn.utils import shuffle
new_input_data, new_Y = shuffle(input_data,Y)

train_x = new_input_data[0:100]
test_x = new_input_data[100:]

train_y = new_Y[0:100]
test_y = new_Y[100:]

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf.fit(train_x, train_y)

prediction = clf.predict(test_x)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(test_y, prediction)

