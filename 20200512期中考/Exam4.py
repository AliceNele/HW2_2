# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:02:10 2020

@author: ASUS
"""

x = [1,2,3]
y = [2,2,2]
'''
x = [1,2,3]
y = ['a','b','c']
'''
ans = []

for i in range(0,len(x)):
    if type(x[i]) == type(y[i]) == True:
         raise AssertionError("x["+i+"]和y["+i+"]型態不同，x["+i+"]型態為 %s，y["+i+"]型態為 %s" %(type(x[i]),type(y[i])))
         
for i in range(0,len(x)):
    if type(x[0]) == type(y[0]):
        
        if x[i] != y[i]:
            ans.append(False)
        else:
            ans.append(True)
        

             
print(ans)