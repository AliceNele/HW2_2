# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:53:59 2020

@author: ASUS
"""

import pandas as pd
import os
path = os.getcwd()#確認資料存的地方
import requests
from io import StringIO
#==========================================
#99-101年
for y in range(99,101+1):
    for m in range(1,12+1):
        folder = './data/' +str(y) + str(m) #要檢查的檔案路徑
        if not os.path.exists(folder):# 查看特定的路徑是否存在，不分檔案或目錄
            os.makedirs(folder) #則創建一個，Python 會連同中間的目錄一起建立

        url = ("https://mops.twse.com.tw/nas/t21/sii/t21sc03_" +str(y) + '_' + str(m) + "_0.html")
        res = requests.get(url)
        res.encoding = 'big5'#99-100年的資料有亂碼的情形
        
        df = pd.read_html(StringIO(res.text))
        for i in range(1,len(df)):
            if ("產業別") in df[i].keys()[0]:
                file_name = df[i].keys()[0].split("：")[1]#檔名為產業名稱
                keys = df[i+1].keys()#產業別的下一個
                col_name = []
                for j in range (0,len(keys)):
                    col_name.append(keys[j][1])
                df[i+1].columns = col_name
                df[i+1].to_csv(os.path.join(folder,file_name + ".csv") , index = False , encoding = "utf-8-sig")#存成csv
#==========================================
#102年1月
folder = './data/1021'
if not os.path.exists(folder):
    os.makedirs(folder)
url = ("https://mops.twse.com.tw/nas/t21/sii/t21sc03_102_1_0.html")
res = requests.get(url)
res.encoding = 'big5'

df = pd.read_html(StringIO(res.text)) 
for i in range(1,len(df)):
    if ("產業別") in df[i].keys()[0]:
        file_name = df[i].keys()[0].split("：")[1]#檔名為產業名稱
        keys = df[i+1].keys()#產業別的下一個
        col_name = []
        for j in range (0,len(keys)):
            col_name.append(keys[j][1])
            
        df[i+1].columns = col_name
        df[i+1].to_csv(os.path.join(folder,file_name + ".csv") , index = False , encoding = "utf-8-sig")#存成csv     
#102年2月-12月
for y in range(102,103):
    for m in range(2,13):
        folder = './data/' +str(y) + str(m)
        if not os.path.exists(folder):
            os.makedirs(folder)
#==========================================
        url = ("https://mops.twse.com.tw/nas/t21/sii/t21sc03_" +str(y) + '_' + str(m) + "_0.html")
        res = requests.get(url)
        res.encoding = 'big5'
        
        df = pd.read_html(StringIO(res.text))
        for i in range(1,len(df)):
            if ("產業別") in df[i].keys()[0]:
                file_name = df[i].keys()[0].split("：")[1]#檔名為產業名稱
                keys = df[i+1].keys()#產業別的下一個
                col_name = []
                for j in range (0,len(keys)):
                    col_name.append(keys[j][1])
                df[i+1].columns = col_name
                df[i+1].to_csv(os.path.join(folder,file_name + ".csv") , index = False , encoding = "utf-8-sig")#存成csv
#==========================================
#103-108年
for y in range(103,109):
    for m in range(1,13):
        folder = './data/' +str(y) + str(m)
        if not os.path.exists(folder):
            os.makedirs(folder)

        url = ("https://mops.twse.com.tw/nas/t21/sii/t21sc03_" +str(y) + '_' + str(m) + "_0.html")
        res = requests.get(url)
        res.encoding = 'big5'
        
        df = pd.read_html(StringIO(res.text))
        for i in range(1,len(df)):
            if ("產業別") in df[i].keys()[0]:
                file_name = df[i].keys()[0].split("：")[1]#檔名為產業名稱
                keys = df[i+1].keys()#產業別的下一個
                col_name = []
                for j in range (0,len(keys)):
                    col_name.append(keys[j][1])
                df[i+1].columns = col_name
                df[i+1].to_csv(os.path.join(folder,file_name + ".csv") , index = False , encoding = "utf-8-sig")#存成csv
#===============================================
#109年的1.2月
for y in range(109,110):
    for m in range(1,3):
        folder = './data/' +str(y) + str(m)
        if not os.path.exists(folder):
            os.makedirs(folder)

        url = ("https://mops.twse.com.tw/nas/t21/sii/t21sc03_" +str(y) + '_' + str(m) + "_0.html")
        df = pd.read_html(url)
        for i in range(1,len(df)):
            if ("產業別") in df[i].keys()[0]:
                file_name = df[i].keys()[0].split("：")[1]#檔名為產業名稱
                keys = df[i+1].keys()#產業別的下一個
                col_name = []
                for j in range (0,len(keys)):
                    col_name.append(keys[j][1])
                df[i+1].columns = col_name
                df[i+1].to_csv(os.path.join(folder,file_name + ".csv") , index = False , encoding = "utf-8-sig")#存成csv
