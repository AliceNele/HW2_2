#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:14:53 2020

最後的「平均損益」，可能因為每個人省略資料的數量不同而異
(我的結果是0.5409%，也有問到0.5407%)
算法用算數平均數，把每一筆資料的損益作加總，最後除以資料數。

@author: peterfu
"""
import json
from funcs import *
#======================================================================================
getJsonFile() #先刪去下市股票資料再開始操作
with open("backtest_targets_remove_delist_target.json", 'r') as f: #讀取資料
    target = json.load(f)
final_ans = [] #儲存題目要求的所有資訊，再存成一個新json檔
total_return = [] #裝所有單筆損益以計算最終平均損益
returnBullish = []
returnBearish = []
#======================================================================================
for i in range(0, len(target)):
    info = {} #設定一個dict用來裝題目要求的資訊
    y = target[i]['year']
    m = target[i]['month']
    bullish_target = target[i]['bullish_target']
    bearish_target = target[i]['bearish_target']
    bullish_price_list = getPrices(y, m, bullish_target)
    bearish_price_list = getPrices(y, m, bearish_target)
    #若有空的則直接略去這筆交易
    if len(bullish_price_list) == 0 or len(bearish_price_list) == 0:
        continue
#======================================================================================
    bullish_open = bullish_price_list[0]
    bullish_close = bullish_price_list[1]
    bearish_open = bearish_price_list[0]
    bearish_close = bearish_price_list[1]
    #做多及做空順序要相反
    bullish_return = ((bullish_close - bullish_open) / bullish_open)
    bearish_return = ((bearish_open - bearish_close) / bearish_open)
    returnBullish.append(bullish_return)
    returnBearish.append(bearish_return)
    total_return.append(bullish_return)
    total_return.append(bearish_return)
#======================================================================================
    info['year'] = y #將所有得出的資料存至先前設定dict
    info['month'] = m
    info['bullish_target'] = bullish_target
    info['bullish_target_open_price'] = bullish_open
    info['bullish_target_close_price'] = bullish_close
    info['bearish_target'] = bearish_target
    info['bearish_target_open_price'] = bearish_open
    info['bearish_target_close_price'] = bearish_close
    final_ans.append(info)#最後將此dict存入先前設定好的list中
#======================================================================================
#存成一個新json檔
with open("HW4_1_outcome.json", 'w') as f:
    json.dump(final_ans, f)
#最終平均損益 = 所有單筆損益的算術平均
average_return = (sum(total_return) / len(total_return)) * 100
#印出結果
print("最終平均損益 = %.4f%%" % average_return) 
#======================================================================================
average_return = (sum(total_return) / len(total_return)) * 100
#印出結果
print("最終平均損益 = %.4f%%" % average_return) 