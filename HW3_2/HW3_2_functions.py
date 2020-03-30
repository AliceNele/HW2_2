# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:56:25 2020
HW2_2_functions.py
@author: Alice Cheng
"""
from HW3_2_class import *
import pickle
import os

def create_credit_user(): # 創信用卡帳戶
    name = input("請輸入姓名: ")
    idnumber = input("請輸入身分證字號: ")
    if (idnumber + ".pkl") in os.listdir("./info/credit"): # 先用身分證字號檢查是否已有可用帳戶
        print("已有可用帳戶")
    else: #沒有可用帳戶，繼續輸入信用額度
        credit = int(input("請輸入信用額度: "))
        data = CreditCardAccount(name, idnumber, credit) # 把資料存到data裡面
        with open('./info/credit/'+ idnumber +".pkl","wb") as info:
            pickle.dump(data, info)

def create_bank_user(): # 創銀行帳戶
    name = input("請輸入姓名: ")
    idnumber = input("請輸入身分證字號: ")
    if (idnumber + ".pkl") in os.listdir("./info/bank"):#先用身分證字號檢查是否已有可用帳戶
        print("已有可用帳戶")
    else: #沒有可用帳戶，繼續輸入密碼
        password = input("請輸入密碼: ")
        check = check_password(password)
        while  check != True:
            password = input("密碼不符合規定，請重新輸入: ")
            check = check_password(password)
        data = BankAccount(name, idnumber, password)
        with open('./info/bank/'+idnumber+'.pkl','wb') as info:
            pickle.dump(data, info)

def check_password(password): # 檢查密碼
    output = True
    if len(password) < 6 or len(password) >20:
        output = False

    flag_num = False
    flag_big = False
    flag_small = False
    for i in password:
        if 48 <= ord(i) and ord(i) <= 57: # 檢查是否至少有一個數字
            flag_num = True
        elif 65 <= ord(i) and ord(i) <= 90: # 檢查是否有至少一個英文大寫
            flag_big = True
        elif 97 <= ord(i) and ord(i) <= 122: # 檢查是否有至少一個英文小寫
            flag_small = True
    if flag_num != True or flag_big != True or flag_small != True:
        output = False

    list1 = list(set(password)) #測試是否三個字母相連
    c = []
    for i in range(0,len(list1)):
        c.append(list1[i]*3)
    for i in range(0,len(c)):
        if c[i] in password:
            output = False
    else:
        return output

def pay_creditcard_fee():
    idnumber = input("請輸入身分證字號: ")
    #檢查是否有銀行跟信用卡帳戶
    if ((idnumber + ".pkl") in os.listdir("./info/bank/")) and ((idnumber + ".pkl") in os.listdir("./info/credit/")): 
        password = input("儲蓄存款帳戶密碼: ")
        with open('./info/bank/'+idnumber + '.pkl','rb') as info: #開啟資料
            user = pickle.load(info)
        if password != user.password:#檢查密碼是否正確，情況3
            print("密碼錯誤")
        else: #密碼對了
            print("密碼答對")
            with open('./info/bank/'+idnumber + '.pkl','rb') as info: #開啟銀行資料
                user = pickle.load(info)
            with open('./info/credit/'+idnumber + '.pkl','rb') as info: #開啟信用卡資料
                account = pickle.load(info)
            if user.inmoney >= account.used:  #儲蓄帳戶餘額 > 信用卡費，情況4
                print("繳費前餘額: %d" % user.inmoney)
                user.inmoney -= account.used   #從儲蓄帳戶扣款繳清卡費
                account.used = 0               #將卡費清空
                print("繳費後餘額: %d" % user.inmoney)
                  #不確定還需不需要存檔這個動作
               #with open('./info/bank/'+idnumber+'.pkl','wb') as info:
                   #pickle.dump(data, info)

            else: #儲蓄帳戶餘額不足，情況5
                print( "餘額不足")
    #有銀行但沒有信用卡帳戶，情況2
    elif ((idnumber + ".pkl") in os.listdir("./info/bank/")) and ((idnumber + ".pkl") not in os.listdir("./info/credit/")): 
        print( "無須繳費")
    #沒有銀行但有信用卡帳戶，情況1
    elif ((idnumber + ".pkl") not in os.listdir("./info/bank/")) and ((idnumber + ".pkl") in os.listdir("./info/credit/")):
        print("請先開立帳戶")
        create_bank_user()