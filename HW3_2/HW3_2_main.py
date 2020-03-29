# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:56:54 2020
HW2_2_main.py
@author: Alice Cheng
"""

from HW3_2_class import*
from HW3_2_functions import*
import pickle

choice = str(input("(a) 新增信用卡帳戶 (b) 新增儲蓄存款帳戶 (c) 更新或查詢帳戶情況 (d) 繳信用卡費: "))
if choice == "a":
    create_credit_user() #回去執行 開立信用卡帳戶

elif choice == "b":
    create_bank_user() #回去執行 開立銀行帳戶

elif choice == "c":
    idnumber = input("請輸入身分證字號: ")
    print("(1) 查詢信用卡可用餘額 ")
    print("(2) 新增信用卡消費金額")
    print("(3) 查詢儲蓄存款帳戶密碼")
    print("(4) 查詢儲蓄存款帳戶餘額")
    print("(5) 存款")
    print("(6) 提款")

    option = input("請選擇欲執行之功能： ")
    if option == "1" or option == "2": # 信用卡功能
        try:
            with open('./info/credit/'+idnumber + '.pkl','rb') as info:
                account = pickle.load(info)

                if option == "1": #查詢信用卡可用餘額
                    balance = account.getBalance()
                    print("可用餘額為: %d" % balance)

                elif option == "2": #新增信用卡消費金額
                    amount = int(input("請輸入消費金額: "))
                    account.consume(amount)
                    with open('./info/credit/'+idnumber + '.pkl','wb') as info:
                        pickle.dump(account,info)

        except FileNotFoundError:
            print("請先開立帳戶")
            create_credit_user()

    if option == "3" or option == "4" or option == "5" or option == "6":
        #file_list = os.listdir('info')
        try:
            with open('./info/bank/' + idnumber + '.pkl','rb') as info:
                user = pickle.load(info)

                if option == "3": #查詢儲蓄存款帳戶密碼
                    print("密碼為: %s" %(user.password))

                elif option == "4": #查詢儲蓄存款帳戶餘額
                    print("餘額為: %s" % (user.asknalance()))

                elif option == "5": #存款
                    amount = int(input("請輸入存入金額: "))
                    user.save_money(amount)
                    with open('./info/bank/' + idnumber + '.pkl','wb') as info:
                        pickle.dump(user,info)
                    print("餘額為: %s" % (user.askbalance()))

                elif option == "6": # 提款
                    take_money = int(input("請輸入提出金額: "))
                    if user.inmoney > take_money:
                        user.withdraw(take_money)
                        with open('./info/bank/' + idnumber + '.pkl','wb') as info:
                            pickle.dump(user,info)
                        print("餘額為: %s" % user.askbalance())
                    else: # 跟他說都不夠額度了還敢花錢啊
                        print("沒那麼多錢還改提這麼多啊")

        except FileNotFoundError:
            print("請先開立帳戶")
            create_bank_user() #回去執行 開立銀行帳戶
elif choice == "d":
    pay_creditcard_fee()

