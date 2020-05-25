# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:14:31 2020

@author: CJ
"""


import pandas as pd
data = pd.read_csv("HW7_2.csv")

Y = data['fraud_ind']
X = data.drop(['fraud_ind'],axis=1)
#把不是數字的做轉換
ecfg = pd.get_dummies(X.ecfg)
flbmk = pd.get_dummies(X.flbmk)
flg_3dsmk = pd.get_dummies(X.flg_3dsmk)
insfg = pd.get_dummies(X.insfg)
ovrlt = pd.get_dummies(X.ovrlt)
#把沒用的資料剔除掉
X = X.drop(['flbmk'],axis=1)
dummy_ecfg = ecfg["Y"].tolist()
dummy_flg_3dsmk = flg_3dsmk["Y"].tolist()
dummy_insfg = insfg["Y"].tolist()
dummy_ovrlt = ovrlt["Y"].tolist()

X['ecfg'] = dummy_ecfg
X['flg_3dsmk'] = dummy_flg_3dsmk
X['insfg'] = dummy_insfg
X['ovrlt'] = dummy_ovrlt
#==========到這邊資料整理好=============

#=========train 的
#個別取出0和1
X_1 = X[0:1099+1] 
X_0 = X[1100:]
#train 的資料，500+500
X_1_train_500 =X_1.sample(n=500, replace=False,random_state=None, axis=0)
X_0_train_500 =X_0.sample(n=500, replace=False,random_state=None, axis=0)
#拼接
c = pd.concat( [X_1_train_500, X_0_train_500], axis=0 )
train_data =c.sort_index()
index1 = train_data.index.values.tolist()
bins = train_data.values.tolist() #train 的1000個
train_Y = []
for i in range(0,len(index1)):
    train_Y.append(Y.iloc[index1[i]]) #到這邊整理完
#==========test的
#test 的資料，50+50
X_1_test_50 =X_1.sample(n=50, replace=False,random_state=None, axis=0)
X_0_test_50 =X_0.sample(n=50, replace=False,random_state=None, axis=0)
#拼接
c = pd.concat( [X_1_test_50, X_0_test_50], axis=0 )
test_data =c.sort_index()
index2 = test_data.index.values.tolist()
bins = test_data.values.tolist() #test 的100個
test_Y = []
for i in range(0,len(index2)):
    test_Y.append(Y.iloc[index2[i]]) #到這邊整理完


#=================
from sklearn.utils import shuffle
new_train_data,new_train_t = shuffle(train_data,train_Y)
new_test_data,new_test_t = shuffle(test_data,test_Y)
#訓練
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(new_train_data, new_train_t)
prediction = clf.predict(test_data)

#===========

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(test_Y, prediction)
print("準確度：" + str(accuracy))
