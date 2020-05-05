# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:14:16 2020
HW6_1
利用正規運算式(re)，驗證帳號密碼是否符合條件
帳號:英文字母、數字、半形句號
密碼：八個字元以上、且包含英文字母、數字和符號(除了數字字母以外的)
@author: Alice Cheng
"""
import re
account = input("請輸入帳號： ")
#帳號部分
pattern_test = r"(\W)"
temp = re.findall(pattern_test,account)
result1 = []
for i in range(0,len(temp)):
    if temp[i] != '.':
        result1.append(temp[i]) # 因為.是可以的，所以手動不見
    
# 不符合規則的部分，如：jfiofj...//3829，會輸出['/', '/']
#=====================================================
#密碼部分
import re

pattern = "^(?=.*\d)(?=.*[a-zA-Z])(?=.*\W).{8,}$" # 至少包含英文字母、數字、符號
password =input("請輸入密碼： ")                   # 老師題目沒有規定至少要一個大小寫英文
result2 = re.findall(pattern, password)

#===============================
flag = 0 
if len(result1) >0: 
    print("帳號格式錯誤")
    flag +=1
if len(result2) != len(password):
    print("密碼格式錯誤")
    flag +=1
if flag == 0:
    print("通過測試")