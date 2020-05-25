# -*- coding: utf-8 -*-
# @author: Alice

class CreditCardAccount:
    def __init__(self, name, phone ,limit):
        self.name = name        # 用戶姓名
        self.phone = phone      # 用戶連絡電話
        self.limit = limit      # 用戶人信用額度
        self.used = 0

    def spending(self, amount):
        if self.used + amount <= self.limit:    # 要花的錢還在信用額度內
            self.used = self.used + amount      # 把消費的錢從額度內扣掉
        else: # 跟他說都不夠額度了還敢花錢啊
            print("無法新增消費,已超過信用額度")
    def getBalance(self):
        return self.limit - self.used

