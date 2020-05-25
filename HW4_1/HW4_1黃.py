#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:48:56 2020

@author: larry
"""
import json 
import datetime
from dateutil.relativedelta import *
import pandas as pd


bad_target = []
with open('backtest_targets_remove_delist_target.json','r') as f:  #讀檔
    target = json.load(f)

for j in range(0,len(target)):    
    y = str(int(target[j]['year']) + 1911)  #更改時間格式
    if len(target[j]['month']) < 2:
        target[j]['month'] = '0' + target[j]['month']
    
    open_day = datetime.datetime.strptime(y + '-' + target[j]['month'] + '-11','%Y-%m-%d') + relativedelta(months=+1)
    close_day = datetime.datetime.strptime(y + '-' + target[j]['month'] + '-10','%Y-%m-%d') + relativedelta(months=+2)

    price_data = pd.read_csv('./data/price/' + target[j]['bullish_target'] + '.csv')
    price_data = price_data.dropna()
    date_list = price_data['Date'].tolist()
    start_date = datetime.datetime.strftime(open_day,'%Y-%m')
    end_date = datetime.datetime.strftime(close_day,'%Y-%m')

    check_start = 0
    check_end = 0
    for i in range(0,len(date_list)):       #取得開始日與結束日
        if check_start == 0 and start_date in date_list[i]:
            start_idx = i
            check_start = 1
        elif check_end == 0 and end_date in date_list[i]:
            check_end = 1
        elif check_end == 1 and end_date not in date_list[i]:
            end_idx = i
            break
        elif check_end == 1 and end_date in date_list[len(date_list)-1]:
            end_idx = len(date_list) - 1
    if check_start == 0 or check_end == 0:
        bad_target.append(target[j]['bullish_target'])
    else:
        trade_range = price_data.iloc[start_idx:end_idx]
        trade_date_list = trade_range['Date'].tolist()
        for i in range(0,len(trade_date_list)):
            trade_date_list[i] = datetime.datetime.strptime(trade_date_list[i],'%Y-%m-%d')
    
        open_delta = []
        close_delta = []
        for i in range(0,len(trade_date_list)):
            open_delta.append(abs(trade_date_list[i] - open_day))
            if trade_date_list[i] > close_day:
                continue
            else:
                close_delta.append(abs(trade_date_list[i] - close_day))
                
        open_indices = [i for i,x in enumerate(open_delta) if x == min(open_delta)]
        close_indices = [i for i,x in enumerate(close_delta) if x == min(close_delta)]
        
        
        open_idx = open_indices[-1]
        close_idx = close_indices[-1]
        
        trade_range = trade_range.reset_index()
        open_price = trade_range['Adj Close'][open_idx]
        close_price = trade_range['Adj Close'][close_idx]
        target[j].update({'bullish_target_open_price':open_price,'bullish_target_close_price':close_price}) #更新資料
with open('backtest_targets_remove_delist_target.json',"w") as f:       #存檔
    json.dump(target,f)
   
for j in range(0,len(target)):    
    y = str(int(target[j]['year']) + 1911)
    if len(target[j]['month']) < 2:
        target[j]["month"] = '0' + target[j]["month"]
    
    open_day1 = datetime.datetime.strptime(y + '-' + target[j]['month'] + '-11','%Y-%m-%d') + relativedelta(months=+1)
    close_day1 = datetime.datetime.strptime(y + '-' + target[j]['month'] + '-10','%Y-%m-%d') + relativedelta(months=+2)

    price_data1 = pd.read_csv('./data/price/' + target[j]['bearish_target'] + '.csv')
    price_data1 = price_data1.dropna()
    date_list1 = price_data1["Date"].tolist()
    start_date1 = datetime.datetime.strftime(open_day1,'%Y-%m')
    end_date1 = datetime.datetime.strftime(close_day1,'%Y-%m')
    check_start1 = 0
    check_end1 = 0
    for i in range(0,len(date_list1)):
        if check_start1 == 0 and start_date1 in date_list1[i]:
            start_idx1 = i
            check_start1 = 1
        elif check_end1 == 0 and end_date1 in date_list1[i]:
            check_end1 = 1
        elif check_end1 == 1 and end_date1 not in date_list1[i]:
            end_idx1 = i
            break
        elif check_end1 == 1 and end_date1 in date_list1[len(date_list1)-1]:
            end_idx1 = len(date_list1) - 1
    if check_start1 == 0 or check_end1 == 0:
        bad_target.append(target[j]['bearish_target'])
    else:
        trade_range = price_data1.iloc[start_idx1:end_idx1]
        trade_date_list = trade_range['Date'].tolist()
        for i in range(0,len(trade_date_list)):
            trade_date_list[i] = datetime.datetime.strptime(trade_date_list[i],'%Y-%m-%d')
    
        open_delta = []
        close_delta = []
        for i in range(0,len(trade_date_list)):
            open_delta.append(abs(trade_date_list[i] - open_day1))
            if trade_date_list[i] > close_day1:
                continue
            else:
                close_delta.append(abs(trade_date_list[i] - close_day1))
                
        open_indices = [i for i,x in enumerate(open_delta) if x == min(open_delta)]
        close_indices = [i for i,x in enumerate(close_delta) if x == min(close_delta)]
        
        
        open_idx1 = open_indices[-1]
        close_idx1 = close_indices[-1]
        
        trade_range = trade_range.reset_index()
        open_price1 = trade_range['Adj Close'][open_idx1]
        close_price1 = trade_range['Adj Close'][close_idx1]
        target[j].update({'bearish_target_open_price':open_price1,'bearish_target_close_price':close_price1})
with open('backtest_targets_remove_delist_target.json',"w") as f:
    json.dump(target,f)

for i in range(0,len(target)):      #無資料時新增NaN
    if len(target[i]) != 8:
        target[i].update({'bullish_target_open_price':'NaN','bullish_target_close_price':'NaN','bearish_target_open_price':'NaN','bearish_target_close_price':'NaN'})
        with open('backtest_targets_remove_delist_target.json','w') as f:
            json.dump(target,f)
           

 
bullish_return = []
bearish_return = []

with open('backtest_targets_remove_delist_target.json','r') as f:       #讀檔
    target = json.load(f)
    for i in range(0,len(target)):
        if target[i]['bullish_target_open_price'] == 'NaN' or target[i]['bullish_target_close_price'] == 'NaN' or target[i]['bearish_target_open_price'] == 'NaN' or target[i]['bearish_target_close_price'] == 'NaN':
            continue
        bullish_return.append((target[i]['bullish_target_close_price']-target[i]['bullish_target_open_price'])/target[i]['bullish_target_open_price'])
        bearish_return.append((target[i]['bearish_target_open_price']-target[i]['bearish_target_close_price'])/target[i]['bearish_target_open_price'])

avg_return = sum(bullish_return + bearish_return)/len(bullish_return+bearish_return)        #計算平均損益

print(avg_return*100,'%')

import pickle
file = open('bullish_return.pickle','wb')
pickle.dump(bullish_return,file)
file.close()

file = open('bearish_return.pickle','wb')
pickle.dump(bearish_return,file)
file.close()




   
