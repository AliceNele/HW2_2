# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 02:20:10 2020
HW4_1
@author: Alice Cheng
"""
from func import *
import json
import time
import datetime
from dateutil.relativedelta import *
import pandas as pd
import pickle
#main
#將下市的排除，並蓋掉資料
with open("backtest_targets_remove_delist_target.json","r") as f:
    target = json.load(f)
# 先弄成list
t = ['1704','1715','2856','3598','4733','3315','6145','2837']
new_data = []
for i in range(0,len(target)):
    if (target[i]['bullish_target'] in t) or target[i]["bearish_target"] in t:
        continue
    
    y = str( int(target[i]["year"]) + 1911 )
    if len(target[i]["month"]) < 2: # 1-9月份前面加0
        m = "0" + target[i]["month"]
    #找資料，這邊跟老師依樣
    bullish_price = select_data(y, m, target[i],"bullish_target")
    bearish_price = select_data(y, m, target[i],"bearish_target")
    
        
    dic = {}
    dic["year"] = target[i]["year"]
    dic["month"] = target[i]["month"]
    dic["bullish_target"] = target[i]["bullish_target"]
    dic["bullish_target_open_price"] = bullish_price[0]
    dic["bullish_target_close_price"] = bullish_price[1]
    dic["bearish_target"] = target[i]["bearish_target"]
    dic["bearish_target_open_price"] = bearish_price[0]
    dic["bearish_target_close_price"] = bearish_price[1]
    
    new_data.append(dic)

with open("backtest_targets_with_price.json", "w") as outfile:
    json.dump(new_data, outfile)    

#============================================================================

#計算最終平均損益
#最終平均損益 = 所有單筆損益的算術平均，寫在　func中
calculate_return()