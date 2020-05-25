# -*- coding: utf-8 -*-
"""
Created on Tue May 12 01:04:35 2020

@author: ASUS
"""

import pandas as pd
import os
path = os.getcwd()#確認資料存的地方
import requests
import time
from io import StringIO
#==========================================

for y in range(99,110):
    for m in range(1,13):
        folder = './data/earning/' +str(y) +"_" +str(m) #要檢查的檔案路徑
        if not os.path.exists(folder):# 查看特定的路徑是否存在，不分檔案或目錄
            os.makedirs(folder) #則創建一個，Python 會連同中間的目錄一起建立

        url = ("https://mops.twse.com.tw/nas/t21/sii/t21sc03_" +str(y) + '_' + str(m) + "_0.html")
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        res = requests.get(url,headers = headers)
        res.encoding = 'big5'#99-100年的資料有亂碼的情形
        
        df = pd.read_html(StringIO(res.text),encoding='big-5')
        i = 0
        
        while i < len(df):
            if ("產業別") in str(df[i].keys()[0]):
                try:
                    #102 以前的不同
                    file_name = df[i].keys()[0].split("：")[1]#檔名為產業名稱
                except:
                    file_name = df[i].keys()[0][0].split("：")[1]#檔名為產業名稱
                
                keys = df[i+1].keys()#產業別的下一個
                col_name = []
                for j in range (0,len(keys)):
                    col_name.append(keys[j][1])
                df[i+1].columns = col_name
                df[i+1].to_csv(os.path.join(folder,file_name + ".csv") , index = False , encoding = "utf-8-sig")#存成csv
                
                i = i+2
            else:
                i = i+1
                
                
                
                
                
                
                