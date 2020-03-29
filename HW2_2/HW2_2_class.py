# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:54:48 2020
HW2_2_class.py
@author: Alice Cheng
"""

#class.py
class Customer:
    def __init__(self, name = str(), idnumber = str()):
        self.name = name #用戶姓名
        self.idnumber = idnumber #用戶身分證字號

class CreditCardAccount(Customer): #信用卡帳戶
    def __init__(self, name = str(), idnumber = str(), credit = int()):
        Customer.__init__(self, name, idnumber)
        self.credit = credit #用戶人信用額度
        self.used = 0

    def consume(self, amount):
        if self.used + amount <= self.credit:
            self.used = self.used + amount
        else:
            print("無法新增消費，已超過信用額度")

    def getBalance(self): #剩餘用額
        return self.credit - self.used

class BankAccount(Customer): #儲蓄存款，提款、存款
    def __init__(self, name = str(), idnumber = str(), password = str()):
        Customer.__init__(self,name,idnumber)
        self.inmoney = 0
        self.password = password #用戶人密碼

    def save_money(self, save_money): #(5)存款
        self.inmoney += save_money

    def withdraw(self, take_money):  #(6)提款
        self.inmoney -= take_money

    def getpassword(self):
        return self.password

    def askbalance(self):
        return self.inmoney
