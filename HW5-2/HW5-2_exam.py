# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 00:28:18 2020
HW5-2
@author: Alice Cheng
"""
# basic
import numpy as np
import pandas as pd
#visual
import matplotlib.pyplot as plt
#導入蠟燭圖套件
import mpl_finance as mpf
from HW3_1_for_5_2 import *
#====================================
#讀資料
getPriceData(ticker,start,end)
'''
#讀取資料

ticker = ("2330")
start = ("2020-03-16") 
end = ("2020-03-20")
'''
data = pd.read_csv("./data/price/"+ticker+".csv")
data1 = data[data["Date"].between(start,end)] # 抓出需要的時間
data1.set_index('Date',inplace=True)

#=========================================
'''
#創建圖框

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1,1,1)

ax.set_xticks(range(0, len(data1.index)))
ax.set_xticklabels(data1.index,rotation = 45)

mpf.candlestick2_ochl(ax, data1['Open'], data1['Close'], data1['High'],data1['Low'], width=0.4, colorup='g', colordown='r', alpha=0.9)

plt.title("Daily Candlestick of %s" %ticker)
plt.xlabel("Date")
plt.ylabel("Price")

ax.set_facecolor('gainsboro')
ax.grid(color='w', linestyle='-', linewidth=3,alpha=0.3)  

#存檔
ax.savefig("%s.pdf" %ticker,format = "pdf")

#plt.show()
'''
#==========================================

plt.figure()


plt.plot(data1['Open'],color = 'r', label="Open")
plt.plot(data['Low'],color = 'g', label="Low")
plt.plot(data['High'],color = 'b', label="High")
plt.plot(data['Close'],color = 'y', label="Close")



# 設定圖片標題，以及指定字型設定，x代表與圖案最左側的距離，y代表與圖片的距離

plt.title("2330 from 2020-03-16 to 2020-03-20", x=0.5, y=1.03)

plt.xticks(fontsize=20)

plt.yticks(fontsize=20)
data1.index = pd.to_datetime(data1.Date)
# 標示x軸(labelpad代表與圖片的距離)

plt.xlabel("Date", fontsize=30, labelpad = 15)

# 標示y軸(labelpad代表與圖片的距離)



# 顯示出線條標記位置

plt.legend()

# 畫出圖片

plt.show()

 







