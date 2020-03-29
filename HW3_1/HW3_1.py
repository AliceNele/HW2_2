# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:28:55 2020
HW3_1
@author: Alice Cheng
"""
import urllib.request
import pandas as pd
import requests
from io import StringIO
import time 
import json
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
url = ("https://finance.yahoo.com/quote/" + str(ticker) +".TW/history?period1= "+ str(start2) +"&period2=" +str( end2) + "&interval=1d&filter=history&frequency=1d")

req = requests.get(url) # 請求
html_df = pd.read_html(req)



#=====================================
