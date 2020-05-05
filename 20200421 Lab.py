# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:20:03 2020

@author: ASUS
"""
#驗證身分證
import re
string = input("請輸入身份證字號： ")
pattern = r"[A-Z]\d{9}" # r"[A-Z][0-9]{9}$"
result = re.search(pattern,string)
print(result)
if result == None:
    print("不符合規定")
else: 
    print("對")
'''
import re
string = input("請輸入身份證字號： ")
if re.match(r"[A-Z][0-9]{9}$,string):
    print("正確")
else:
    print("錯誤")
'''