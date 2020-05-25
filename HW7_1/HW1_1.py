# -*- coding: utf-8 -*-
# @author: Alice

import pickle
import os
from CreditCardAccount import CreditCardAccount

data_folder = "Data"
credit_data_folder = os.path.join(data_folder, "CreditCard")
if not os.path.exists(credit_data_folder):
    os.makedirs(credit_data_folder)

choice = input("(a) 新增客戶資料，(b) 新增消費紀錄，(c) 確認信用卡剩餘額度: ")
name = input("請輸入姓名: ")
filename = name + ".pkl"
filename = os.path.join(credit_data_folder, filename)

if choice == "a":
    phone = input("請輸入連絡電話: ")
    limit = int(input("請輸入信用額度: "))
    newAccount = CreditCardAccount(name, phone, limit)
    with open(filename, 'wb') as f:
        pickle.dump(newAccount, f)

elif choice == "b":
    with open(filename, 'rb') as f:
        account = pickle.load(f)
    amount = int(input("請輸入新增消費金額: " ))
    account.spending(amount)
    with open(filename, 'wb') as f:
        pickle.dump(account,f)

elif choice == "c":
    with open(filename, 'rb') as f:
        account = pickle.load(f)
    balance = account.getBalance()
    print(balance)
