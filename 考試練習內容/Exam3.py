# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:13:50 2020

@author: ASUS
"""

import pickle
class CreditCardAccount:
    def __init__(self, name, phone ,limit):
        self.name = name #用戶姓名
        self.phone = phone #用戶連絡電話
        self.limit = limit #用戶人信用額度
        self.used = 0

   
    def spending(self,amount):  
        if self.used + amount <= self.limit: # 要花的錢還在信用額度內
            self.used = self.used + amount #把消費的錢從額度內扣掉
        else: # 跟他說都不夠額度了還敢花錢啊
            print("無法新增消費,已超過信用額度")
    def getBalance(self):
        return self.limit - self.used


choice =  input("(a) 新增客戶資料，(b) 新增消費紀錄，(c) 確認信用卡剩餘額度: ")  
if choice == "a": 
    name = (input("請輸入姓名: "))
    phone = input("請輸入連絡電話: ")
    limit = int(input("請輸入信用額度: "))
    newAccount = CreditCardAccount(name,phone,limit)
    
    with open('./CreditCardData/'+name +".pkl",'wb') as f:
        pickle.dump(newAccount,f)
        
elif choice == "b":
    name = input("請輸入姓名: ")
    with open('./CreditCardData/'+name +".pkl",'wb') as f:
        account = pickle.load(f)
    
    amount = int(input("請輸入新增消費金額: " ))
    account.spending(amount)
    
    with open('./CreditCardData/'+name +".pkl",'wb') as f:
        pickle.dump(account,f)
        
elif choice == "c":
    name = input("請輸入姓名: ")
    try:
        with open('./CreditCardData/'+name +".pkl",'wb') as f:
            account = pickle.load(f)
    except:
        print("查無用戶資料，請新增用戶")
        phone = input("請輸入連絡電話: ")
        limit = int(input("請輸入信用額度: "))
         newAccount = CreditCardAccount(name,phone,limit)
    
        with open('./CreditCardData/'+name +".pkl",'wb') as f:
            pickle.dump(newAccount,f)
    else:
        phone = input("請輸入連絡電話: ")
        if phone != account.phone:
            ptint("號碼錯誤")
        else:
        
            balance = account.getBalance()
            print(balance)
        
        
    