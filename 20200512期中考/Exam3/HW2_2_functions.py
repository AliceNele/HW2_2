# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:56:25 2020
HW2_2_functions.py
@author: Alice Cheng
"""
from HW2_2_class import *
import pickle
import os
import re
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
    if len(password) < 10 :
        output = False

    flag_num = False
    flag_big = False
    flag_small = False
    pattern = r"\W"
    flag_marks = False
    for i in password:
        if 48 <= ord(i) and ord(i) <= 57: # 檢查是否至少有一個數字
            flag_num = True
        elif 65 <= ord(i) and ord(i) <= 90: # 檢查是否有至少一個英文大寫
            flag_big = True
        elif 97 <= ord(i) and ord(i) <= 122: # 檢查是否有至少一個英文小寫
            flag_small = True
        elif re.search(pattern,i) != None:  # 測試符號
            flag_marks = True
    if flag_num != True or flag_big != True or flag_small != True or flag_marks != True:
        output = False

    list1 = list(set(password)) #測試是否三個字母相連
    c = []
    for i in range(0,len(list1)):
        c.append(list1[i]*3)
    for i in range(0,len(c)):
        if c[i] in password:
            output = False
            
    return output
