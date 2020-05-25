# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:28:55 2020

HW3_1 又修改成4-1的func

@author: Alice Cheng
"""
import urllib.request
import os
import time 
import pandas as pd
import time
import datetime
from dateutil.relativedelta import *
import json
import pickle
'''
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
'''
#======================================
def select_data(y, m, target, market_type): 
    price_data = pd.read_csv("./data/price/" + target[market_type] + ".csv")
    price_data = price_data.dropna() # 刪除nan的資料
    date_list = price_data["Date"].tolist()
        
    open_day = datetime.datetime.strptime( y + "-" + m + "-11", "%Y-%m-%d") + relativedelta(months=+1)
    close_day = datetime.datetime.strptime( y + "-" + m + "-10", "%Y-%m-%d") + relativedelta(months=+2)
        
    start_date = datetime.datetime.strftime(open_day, "%Y-%m")
    end_date = datetime.datetime.strftime(close_day, "%Y-%m")
                 
    check_start = 0
    check_end = 0
    start_idx = 0
    end_idx = 0
    for j in range(0, len(date_list)):
        if check_start == 0 and start_date in date_list[j]:
            start_idx = j
            check_start = 1
        elif check_end == 0 and end_date in date_list[j]:
            check_end = 1
        elif check_end == 1 and end_date not in date_list[j]:
            end_idx = j
            break

    trade_range = price_data.iloc[start_idx:end_idx]
    trade_date_list = trade_range["Date"].tolist()
    for j in range(0, len(trade_date_list)):
        trade_date_list[j] = datetime.datetime.strptime( trade_date_list[j], "%Y-%m-%d" )
        
    open_delta = []
    close_delta = []
    for j in range(0, len(trade_date_list)):
        open_delta.append(abs(trade_date_list[j] - open_day))
        if trade_date_list[j] > close_day:
            continue
        else:
            close_delta.append(abs(trade_date_list[j] - close_day))
        
    open_indices = [j for j, x in enumerate(open_delta) if x == min(open_delta)]
    close_indices = [j for j, x in enumerate(close_delta) if x == min(close_delta)]
    open_price = "NaN"
    close_price = "NaN"
    
    if open_indices != [] and close_indices != []: # =[] 表示沒有資料
        open_idx = open_indices[-1]
        close_idx = close_indices[-1]
        
        trade_range = trade_range.reset_index()
        open_price = trade_range["Adj Close"][open_idx]
        close_price = trade_range["Adj Close"][close_idx]
    
    return (open_price,close_price)  
#================================================================================
def calculate_return():    #這邊也跟老師依樣
    with open("backtest_targets_with_price.json", "r") as f:
        target = json.load(f)
    
    bullish_return = []
    bearish_return = []
    for i in range(0, len(target)):  # 排除NaN資料
        if  target[i]["bullish_target_open_price"] == "NaN" or \
            target[i]["bullish_target_close_price"] == "NaN" or \
            target[i]["bearish_target_open_price"] == "NaN" or \
            target[i]["bearish_target_close_price"] == "NaN":
             continue
        
        bullish_revenue = (target[i]["bullish_target_close_price"]-target[i]["bullish_target_open_price"])/target[i]["bullish_target_open_price"]
        bearish_revenue = (target[i]["bearish_target_open_price"]-target[i]["bearish_target_close_price"])/target[i]["bearish_target_open_price"]
        bullish_return.append(bullish_revenue)
        bearish_return.append(bearish_revenue)
    
    ave_return = (sum(bullish_return + bearish_return) / len(bullish_return + bearish_return))*100
 
    print("最終平均損益 = %.4f%%" % ave_return)
   
    file = open("bullish_return.pickle","wb")
    pickle.dump(bullish_return, file)
    file.close()
        
    file = open("bearish_return.pickle","wb")
    pickle.dump(bearish_return, file)
    file.close()   
    
    
