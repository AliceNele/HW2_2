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

with open("backtest_targets.json","r") as f:
    target = json.load(f)
    
t = ['3598','4733','3315','6145','2837']
new_data = []
for i in range(0,len(target)):
    if target[i]['bullish_target'] in t or target[i][bearish_target] in t:
        
targey_list = []
for i in range(0,len(target)):
    target_list.append(target[i]['bullish_target'])
    target_list.append(target[i]['bearish_target'])
    
target_set = list(set(target_list))

for i in range(0,len(target_list)):
    
    if i % 30 == 0:
        time.sleep(50) # 每抓 30 筆資料，休息 50 秒
    getPriceData(target_set[i],"2000-01-03","2000-01-03")
    