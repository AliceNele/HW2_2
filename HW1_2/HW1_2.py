# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 01:04:58 2020
程式設計：HW1_2
@author: Alice Cheng
"""

# Variable
Sentence = str(input()) # 輸入句子
NodotSentence = ''

#===============================
# Main
for i in Sentence: # 此處是要只留下英文字母與空白，去掉逗點或是 dot，方便做判斷
    if i.isalpha() or i ==" " :
        NodotSentence += i  

list1 = NodotSentence.split(" ") #將一段文字以空白為界輸入一個 list 中

flag = 0
Firstword = list1[0]

if Firstword.istitle() == False or Firstword.upper() == False: # 檢測第一個詞，是否第一個字母大寫 or 所有字符大寫
    flag +=1

else:
    for i in range(1,len(list1)):
        if (list1[i].islower() == False) and (list1[i].istitle() == False) and (list1[i].isupper() == False):            
            flag += 1
            
        else:
            flag +=0
            
if flag >0:
    print("False")
else:
    print("True")
        
    
    
 