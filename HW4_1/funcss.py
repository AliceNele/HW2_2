# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:24:18 2020

@author: 537
"""

import pandas as pd
import datetime
import json
import pickle
from dateutil.relativedelta import *

#-------------------------------------------------------------------
# 找出交易日期的資料(line16 ~ line67都跟老師講義一樣)
def select_data(y, m, target, market_type): 
    price_data = pd.read_csv("./data/price/" + target[market_type] + ".csv")
    price_data = price_data.dropna() # 刪除nan(null)的資料
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
#-------------------------------------------------------------------
def get_revenue():    
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
        # 報酬率跟老師的算法一樣
        bullish_revenue = (target[i]["bullish_target_close_price"]-target[i]["bullish_target_open_price"])/target[i]["bullish_target_open_price"]
        bearish_revenue = (target[i]["bearish_target_open_price"]-target[i]["bearish_target_close_price"])/target[i]["bearish_target_open_price"]
        bullish_return.append(bullish_revenue)
        bearish_return.append(bearish_revenue)
     
    ave_return = sum(bullish_return + bearish_return) / len(bullish_return + bearish_return)
    #print( sum(bullish_return + bearish_return) )
    print(ave_return)
    # 存檔(HW5用)
    file = open("bullish_return.pkl","wb")
    pickle.dump(bullish_return, file)
    file.close()
        
    file = open("bearish_return.pkl","wb")
    pickle.dump(bearish_return, file)
    file.close()    