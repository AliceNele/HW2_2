# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:16:11 2020
HW5-1
@author: ASUS
"""

import pandas as pd
import pickle
#變成三個
#建立初始圖框
import numpy as np
import matplotlib.pyplot as plt

with open ('bullish_profit.pickle','rb') as file:
    bullish_return = pickle.load(file)
with open ('bearish_profit.pickle','rb') as file:
    bearish_return = pickle.load(file)  

returnlist = bullish_return + bearish_return
fig = plt.figure(figsize=(16,8))
bins = [-1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00]
x = np.arange(1,100)
import random
data = [random.normalvariate(0,0.3) for _ in range(12000)]

'''
ax = fig.add_subplot(311)
#

'''
#fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(3,1,1)
ax.set_xlim(-1.00,1.00) #設定x軸範圍
ax.set_ylim(0,5500) #設定y軸範圍
ax.set_yticks(range(0,5001,5000)) #設定y軸標籤
ax.set_xticks(bins)  #設定x軸標籤
ax.hist(data,bins=bins,linewidth = 1,color = "coral")
plt.title("Results")
#=======================================
ax2 = fig.add_subplot(312)
ax2.set_xlim(-1.00,1.00) #設定x軸範圍
ax2.set_ylim(0,550) #設定y軸範圍
ax2.set_yticks(range(0,501,500)) #設定y軸標籤
ax2.set_xticks(bins)  #設定x軸標籤
ax2.hist(bullish_return,bins=bins,linewidth = 1,color = "coral")
plt.title("Bullish Results")
#========================================
ax3 = fig.add_subplot(313)
ax3.set_xlim(-1.00,1.00) #設定x軸範圍
ax3.set_ylim(0,2200) #設定y軸範圍
ax3.set_yticks(range(0,2001,2000)) #設定y軸標籤
ax3.set_xticks(bins)  #設定x軸標籤
ax3.hist(bearish_return,bins=bins,linewidth = 1,color = "coral")
plt.title("Bearish Results")

plt.tight_layout() #將間距拉開
plt.show()
