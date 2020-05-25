# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:52:32 2020

@author: ASUS
"""

import pandas as pd
data = pd.read_csv("長榮航.txt",sep="\t")
close = pd.DataFrame(data['Close'])
daily_return = close.pct_change(1) #改變百分比

import numpy as np
direction = np.where(daily_return['Close'][1:] >= 0, 1, 0)
windows = 3
'''
# 方法 1
X = []
for i in range(0,len(direction)-windows):
    X.append(direction[i : i + windows])
    
# 方法 2
X = np.array([np.array(direction[ i : i + windows]) for i in range(len(direction)-windows)])
'''
# 方法 3
from numpy.lib.stride_tricks import as_strided
X = as_strided(direction, shape=(len(direction)-windows, windows), strides= (direction.strides[0],direction.strides[0]))
Y = direction[3:]

train_x = X[0:4000]
test_x = X[4000:]

train_y = Y[0:4000]
test_y = Y[4000:]
from sklearn import svm
clf = svm.SVC()
clf.fit(train_x, train_y)

prediction = clf.predict(test_x)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(test_y, prediction)


'''

from sklearn import tree
X = [[0,0],[1,1]]
Y = [0,1]
clf= tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

prediction = clf.predict([[2., 2.]])
probability = clf.predict_proba([[2., 2.]])

#======================

