# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:08:11 2020

@author: ASUS
"""
'''
x = [1,2,3]
y = "Apple"
try:
    #TypeError
    #x[0] + y[0]
    
    #IndexError
    #print(x[10]) #印出 list index out of range
    
    #NameError
    a(x,y) 
    
    #ZeroDivisionError
    #b = 4/0
    
    #No exception
    #c = 1 + 1
    
except TypeError:
    print("E1")
except IndexError as e:
    print(e)
except(NameError,KeyError): #如果是name or key
    #except(NameError,KeyError,.....):
    print("E3") #因為我們沒有定義 a，
except: #有錯誤，但不再上述的錯誤裡
    print("E4")
else: #try 裡面沒有任何錯誤
    print("No Exception")
finally:# 不管如何都要印出
    print("Finally")

#========================================

def raiseError1():
    raise IndexError
    
raiseError1()

def raiseError2():
    raise IndexError("Error 2")
    
raiseError2()

#==================================

a = input("請輸入一個數字：")
if not a.isdigit():
    raise ValueError("a 必須是數字")

#=======================================
#ex1

assert a
#ex2
a = 1
assert a < 0, "a must be negative"

#========================

class MyBad(Exception):
    def __str__(self):
        return "Sorry! My mistask!"
    
a = 1
b = 2
if a!= b :
    raise MyBad #MyBad: Sorry! My mistask!

#=================================
#跳出兩個迴圈
#方法一
while True:
    for i in range(0,10):
        if i > 3:
            break
        print(i)
    else: #接的是 for 沒錯
        continue
    break

#方法2
class  Exitloop(Exception):
    pass

try:
    while True:
        for i in range(0,10):
            if i > 3:
                raise Exitloop
            print(i)
except Exitloop:
    print("Stop")
'''
#==================
import traceback
def inverse(x):
    return 1/x
try:
    inverse(0)
    
except:
    traceback.print_exc(file = open("9_traceback.exc","w"))














