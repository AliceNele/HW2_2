# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 02:20:10 2020
HW4_1
@author: Alice Cheng
"""
from func import *
import json
import time

#main
#將下市的排除，並蓋掉資料
with open("backtest_targets_remove_delist_target.json","r") as f:
    target = json.load(f)
# 先弄成list
t = ['1714','1715','2856','3598','4733','3315','6145','2837']
new_data = []
for i in range(0,len(target)):
    if target[i]['bullish_target'] in t or target[i]["bearish_target"] in t:
        continue
    new_data.append(target[i])
with open('backtest_targets_remove_delist_target.json','w') as outfile:
    json.dump(new_data,outfile)

#重新 load 乾淨的股市資料
with open("backtest_targets_remove_delist_target.json","r") as f:
    target = json.load(f)
target_list = []
for i in range(0,len(target)):
    target_list.append(target[i]['bullish_target'])
    target_list.append(target[i]['bearish_target'])

target_set = list(set(target_list)) # 把重複的弄不見(set會把重複的弄掉)

for i in range(0,len(target_list)):

    if i % 30 == 0:
        time.sleep(70) # 每抓 30 筆資料，休息 50 秒
    getPriceData(target_set[i],"2000-01-03","2000-01-03")
    #將資料放入 dictionary
#=============================================
#找出指定區間的價格資訊
import pandas as pd
import datetime
from dateutil.relativedelta import *

y = '100'
m = '1'
bullish_target = "3406"
bearish_target = "3535"

y = str(int(y) + 1911)
if len(m) < 2:
    m = "0" + m
    
open_day = datetime.datetime.strptime(y + "-" + m + "-11", "%Y-%m-%d") + relativedelta(months=+1)
close_day = datetime.datetime.strptime(y + "-" + m + "-10", "%Y-%m-%d") + relativedelta(months=+2)

price_data = pd.read_csv("./data/price/" + bullish_target + ".csv")

date_list = price_data["Date"].tolist()
start_date = datetime.datetime.strftime(open_day,"%Y-%m")
end_date = datetime.datetime.strftime(close_day,"%Y-%m")

check_start = 0
check_end = 0
for i in range(0,len(date_list)):
    if check_start == 0 and start_date in date_list[i]:
        start_idx = i
        check_start = 1
    elif check_end == 0 and end_date in date_list[i]:
        check_end = 1
    elif check_end == 1 and end_date not in date_list[i]:
        end_idx = 1
        break
print(date_list[start_idx:end_idx])
#==============================================
#找出最近的交易日
trade_range = price_data.iloc[start_idx:end_idx]
trade_date_list = trade_range['Date'].tolist()
for i in range(0,len(trade_date_list)):
    trade_date_list[i] = datetime.datetime.strptime(trade_date_list[i],"%Y-%m-%d")

open_delta = []
close_delta = []
for i in range(0,len(trade_date_list)):
    open_delta.append(abs(trade_date_list[i] - open_day))
    if trade_date_list[i] > close_day:
        continue
    else:
        close_delta.append(abs(trade_date_list[i] - close_day))

open_indices = [i for i, x in enumerate(open_delta) if x == min(open_delta)]
close_indices = [i for i, x in enumerate(close_delta) if x == min(close_delta)]

trade_range = trade_range.reset_index()
open_price = trade_range['Adj Close'][open_idx]
close_price = trade_range['Adj Close'][close_idx]
#==============================================
#計算最終平均損益
with open("backtest_results.json","r") as f:
    target = json.load(f)
bullish_return = []
bearish_return = []
for i in range(0,len(target)):
    if target[i]['bullish_target_open_price'] == "NaN" or \
        target[i]['bullish_target_close_price'] == "NaN" or \
        target[i]['bearish_target_open_price'] == "NaN" or \
        target[i]['bearish_target_close_price'] == "NaN" :
        
        continue
        
    bullish_return.append((target[i]['bullish_target_close_price'] -   \
                         target[i]['bullish_target_open_price'] )/    \
                          target[i]['bullish_target_open_price'])
    
    bearish_return.append((target[i]['bearish_target_open_price'] -   \
                         target[i]['bearish_target_close_price'] )/    \
                          target[i]['bearish_target_open_price'])

ave_return = sum(bullish_return + bearish_return)/len(bullish_return + bearish_return)

import pickle
file = open('bullish_return.pickle','wb')
pickle.dump(bullish_return, file)
file.close()

file = open('bearish_return.pickle','wb')
pickle.dump(bearish_return, file)
file.close()