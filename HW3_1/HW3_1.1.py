# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:28:55 2020
HW3_1
雖然他會跑出這句
FileNotFoundError: [Errno 2] No such file or directory: '.data/price'
但是檔案有被抓下來
@author: Alice Cheng
"""
import urllib.request
import pandas as pd
import requests
import os
path = os.getcwd()#確認資料存的地方
import time 
'''
#======================================
#function
def getPriceData(ticker,start,end):
    timeArraystart = time.localtime()
    
    
# 將輸入的時間轉為電腦能接受的
    #================(v)
    #將 - 消掉
    list_start = start.split("-")
    list_end = end.split("-")
    
    #將上面的 list 轉為 str()
    start1 = " ".join(list_start)
    end1 = " ".join(list_end)
    
    #將上面的 str 轉成秒數
    
    start2 = int(time.mktime(time.strptime(start1,"%Y %m %d"))) #(轉為時戳(把一個格式化時間字串轉化為 struct_time))
    end2 = int(time.mktime(time.strptime(end1,"%Y %m %d")))
    #================(v)
    url = ("https://finance.yahoo.com/quote/" + ticker +".TW/history?period1= "+ start2 +"&period2=" + end2 + "&interval=1d&filter=history&frequency=1d")
    req = requests.get(url) # 請求
    html_df = pd.read_html(req)
#======================================
'''
#urllib.request.urlretrieve(url,)
ticker = 2330
start = "2020-03-16"
end = "2020-03-20"
list_start = start.split("-")
list_end = end.split("-")
    
    #將上面的 list 轉為 str()
start1 = " ".join(list_start)
end1 = " ".join(list_end)
    
    #將上面的 str 轉成秒數
    
start2 = int(time.mktime(time.strptime(start1,"%Y %m %d"))) #(轉為時戳(把一個格式化時間字串轉化為 struct_time))
end2 = int(time.mktime(time.strptime(end1,"%Y %m %d")))
    #================(v)
#url = ("https://finance.yahoo.com/quote/" + str(ticker) +".TW/history?period1= "+ str(start2) +"&period2=" +str( end2) + "&interval=1d&filter=history&frequency=1d")
#創建資料夾
folder = './data/price' #要檢查的檔案路徑
if not os.path.exists(folder):# 查看特定的路徑是否存在，不分檔案或目錄
    os.makedirs(folder)
url = ("https://query1.finance.yahoo.com/v7/finance/download/"+str(ticker) + ".TW?period1="+ str(start2) +"&period2=" +str( end2) + "&interval=1d&events=history")
urllib.request.urlretrieve(url,'.data/price/2330.csv')
#req = requests.get(url) # 請求
#html_df = pd.read_html(req)



#=====================================
