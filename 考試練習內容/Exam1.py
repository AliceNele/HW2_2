# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:23:04 2020

@author: ASUS
"""
 
class Specialist:
    def __init__(self,m):
        self.m = m
        
    def __sub__(self,other):
        ans = []
        
        for i in range(0,len(self.m)):
            ans.append(self.m[i] - other.m[i])
        return ans
a = Specialist([1,2,3])
b = Specialist([3,4,5])
c = a - b
print(c)
#==============================================================================


class A:
    def setA(self,value):
        self.data = value
    def dis(self):
        print(self.data)
class B(A):
    def addone(self):
        self.data +=1
    def dis(self):
        print("display in B: %s"%self.data)

c = A()
c.setA(2)
c.dis()
#c.addone()

d = B()
d.setA(3)
d.addone()
d.dis()












   


