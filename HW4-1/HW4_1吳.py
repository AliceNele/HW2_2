# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:23:44 2020

@author: 537
"""

import json
from funcss import *
#------------------------------------------------------------------
with open("backtest_targets_remove_delist_target.json", "r") as f:
    target = json.load(f)

t = ["1704","1715","2856","3598","4733","3315","6145","2837"] #下市股票
new_data = []
for i in range(0,len(target)): # 刪除下市的投資標的
    if (target[i]["bullish_target"] in t) or (target[i]["bearish_target"] in t):
        continue 
    
    y = str( int(target[i]["year"]) + 1911 )
    if len(target[i]["month"]) < 2: # 將個位數月份前面加0(2月 to 02月)
        m = "0" + target[i]["month"]
    
    # 找出交易日期的資料
    bullish_price = select_data(y, m, target[i],"bullish_target")
    bearish_price = select_data(y, m, target[i],"bearish_target")
    
    tmp = {}
    tmp["year"] = target[i]["year"]
    tmp["month"] = target[i]["month"]
    tmp["bullish_target"] = target[i]["bullish_target"]
    tmp["bullish_target_open_price"] = bullish_price[0]
    tmp["bullish_target_close_price"] = bullish_price[1]
    tmp["bearish_target"] = target[i]["bearish_target"]
    tmp["bearish_target_open_price"] = bearish_price[0]
    tmp["bearish_target_close_price"] = bearish_price[1]
    
    new_data.append(tmp)

with open("backtest_targets_with_price.json", "w") as outfile:
    json.dump(new_data, outfile)    

#------------------------------------------------------------------
get_revenue() # 計算報酬率