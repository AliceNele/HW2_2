# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 01:18:26 2020
程式設計：HW1_1
@author: Alice Cheng
"""


class Bank:
    def __init__(self, name=str(), phone=str(), credit=int(), allusers={}):
        self.name = name #用戶姓名
        self.phone = phone #用戶連絡電話
        self.credit = credit #用戶人信用額度
        self.allusers = allusers #空的字典，這樣就可以把新的用戶存進去

    def create_user(self): #選項 a
        self.name = str(input("請輸入姓名: "))
        self.phone = str(input("請輸入連絡電話: "))
        self.credit = int(input("請輸入信用額度: "))
        new_user = [self.name, self.phone, self.credit]  #做成字典
        self.allusers[self.name] = new_user # 存到字典 allusers
 
    def spending(self):  #選項 b
        insert_name = str(input("請輸入姓名: " ))
        spend_money = int(input("請輸入新增消費金額: " ))
 
        if spend_money <= self.allusers[insert_name][2]: # 要花的錢還在信用額度內
            self.allusers[insert_name][2] -= spend_money #把消費的錢從額度內扣掉
        else: # 跟他說都不夠額度了還敢花錢啊
            print("無法新增消費,已超過信用額度")
 
    def search_user(self): #選項 c
        search_name = str(input("請輸入姓名: "))
        search_phone = str(input("請輸入電話: "))
        if search_name != search_name.allusers[0]:
            my_bank.create_user()
        elif search_phone !=  self.allusers[1]:
            print("號碼錯誤")
        else:
            current_credit = self.allusers[search_name][2]
            print(current_credit)
 
my_bank = Bank() 

choice = ( str( input("(a) 新增客戶資料，(b) 新增消費紀錄，(c) 確認信用卡剩餘額度: ")))
 
if choice == "a": 
    my_bank.create_user() #回去執行 Bank 的 create_user
elif choice == "b":
    my_bank.spending() #回去執行 Bank 的 spending
elif choice == "c":
        my_bank.search_user() ##回去執行 Bank 的 search_user