# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:52:32 2020

@author: ASUS
"""

from sklearn import tree
X = [[0,0],[1,1]]
Y = [0,1]
clf= tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

prediction = clf.predict([[2., 2.]])
probability = clf.predict_proba([[2., 2.]])