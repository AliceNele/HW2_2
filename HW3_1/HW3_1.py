# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:28:55 2020
到時候excel 打開，會看到【Volume】呈現 1.04E+08
把他拉開一些，就會看到跟題目一樣的數字囉~
第一次可以直接先跑，會出現題目例子，
接下來請幫我把那一段註解起來，再跑下面的輸入段，感謝你~
HW3_1

@author: Alice Cheng
"""
import urllib.request
import os
path = os.getcwd()#確認資料存的地方
import time 

#======================================
#function
def getPriceData(ticker,start,end):
    list_start = start.split("-")
    list_end = end.split("-")
    
    #將上面的 list 轉為 str()
    start1 = " ".join(list_start)
    end1 = " ".join(list_end)
    
    #將上面的 str 轉成秒數
    
    start2 = int(time.mktime(time.strptime(start1,"%Y %m %d"))) #(轉為時戳(把一個格式化時間字串轉化為 struct_time))
    end2 = int(time.mktime(time.strptime(end1,"%Y %m %d"))) + 60*60*10

    #創建資料夾
    folder = './data/price' #要檢查的檔案路徑
    if not os.path.exists(folder):# 查看特定的路徑是否存在，不分檔案或目錄
        os.makedirs(folder)
    url = ("https://query1.finance.yahoo.com/v7/finance/download/"+str(ticker) + ".TW?period1="+ str(start2) +"&period2=" +str( end2) + "&interval=1d&events=history")
    urllib.request.urlretrieve(url,'./data/price/'+str(ticker)+ '.csv')

#======================================
#main

ticker = 2330
start = "2020-03-16"
end = "2020-03-20"
getPriceData(ticker,start,end)

'''
ticker = int(input("請輸入台灣股票代碼： ")
start = input("請輸入開始時間")
end = input("請輸入結束時間")
getPriceData(ticker,start,end)
'''