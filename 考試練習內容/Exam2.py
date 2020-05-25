# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:50:57 2020

@author: ASUS
"""
import math
class Bank:
    def __init__(self, name=str(), phone=str(), credit=int(), allusers={}):
        self.name = name #用戶姓名
        self.phone = phone #用戶連絡電話
        self.credit = credit #用戶人信用額度
        self.used = 0

   
    def spending(self,amount):  
        if self.used + amount <= self.credit: # 要花的錢還在信用額度內
            self.used = self.used + amount #把消費的錢從額度內扣掉
        else: # 跟他說都不夠額度了還敢花錢啊
            print("無法新增消費,已超過信用額度")
    def getBalance(self):
        return self.credit - self.used
        
class VIPAccount(Bank):
    def consume(self,amount):
        self.used = self.used + math.floor(0.99 * amount)

Tony = Bank("Tony","gjidfo",30000)
Sandy = VIPAccount("Sandy","fjieo",30000)
Tony.spending(10000)
print(Tony.getBalance())
Sandy.consume(10000)
print(Sandy.getBalance())

Tony.spending(30000)
Sandy.consume(100000)
print(Sandy.getBalance())

