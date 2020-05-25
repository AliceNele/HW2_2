# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:01:08 2020

@author: Alice Cheng
"""

#找出外匯資料，抓近三個月的
import pandas as pd
import pickle
import requests
import os 
from io import StringIO
import datetime
os.getcwd()

#=====================================================
#輸入時間
print("因紀錄關係，最早時間僅能從2020-01-22開始")
start = input("請輸入開始時間(如：2020-01-22)： ")
end = input("請輸入結束時間(如：2020-03-16)﹕")
start_time = datetime.datetime.strptime(str(start), "%Y-%m-%d").date()
end_time = datetime.datetime.strptime(str(end), "%Y-%m-%d").date()
    

#==================================================
#抓外匯資料
folder = "./data"
if not os.path.exists(folder):
    os.makedirs(folder)
url = "https://rate.bot.com.tw/xrt/quote/l6m/USD/"
r = requests.get(url)
#r.encoding='utf-8-sig'
hello = pd.read_html(StringIO(r.text),encoding='utf-8-sig')
    
data = hello[0].iloc[:,0:6]
data.columns = [u"掛牌日期",u"幣別", u"現金買入",u"現金賣出",u"即期買入",u"即期賣出"]
    
data.to_csv(os.path.join(folder,"USD.csv"),encoding="utf-8-sig")
   
#======================================================
#讀取資料

data_1=pd.read_csv("./data/USD.csv")
data_1=data_1.drop(columns=["Unnamed: 0","幣別","現金買入","現金賣出"])

#改變日期格式
for i in range(0,len(data_1.index)):
    a = datetime.datetime.strptime(str(data_1["掛牌日期"][i]), "%Y/%m/%d").date()
    data_1.loc[i,"掛牌日期"] = a

temp = data_1[data_1["掛牌日期"].between(start_time,end_time)] # 抓出需要的時間
temp.set_index("掛牌日期",inplace = True) # 把時間改成　index 
#存進去
USD_buy = []
USD_sell = []
USD_date = []

USD_buy = temp['即期買入'].tolist()
USD_sell = temp['即期賣出'].tolist()
USD_date = temp.index.tolist()

with open("USD_buy.pickle","wb") as f:
    pickle.dump(USD_buy,f)

with open("USD_sell.pickle","wb") as f:
    pickle.dump(USD_sell,f)
    
with open("USD_date.pickle","wb") as f:
    pickle.dump(USD_date,f)

#到此，匯率資料抓取完畢
#=================================================================
#計算價格變化
USD_compare_buy_price = [0,]
USD_compare_sell_price = [0,]
for i in range(1,len(temp)):
    a = (USD_buy[i] - USD_buy[i-1] )/USD_buy[i-1] # 買入價格與昨日比較
    USD_compare_buy_price.append(a)
    b = (USD_sell[i] - USD_sell[i-1])/USD_sell[i-1] #賣出價格與昨日比較
    USD_compare_sell_price.append(b) # 賣出價格與昨日比較
    

f=open("USD_compare_buy_pickle","wb")
pickle.dump(USD_compare_buy_price,f)
with open("USD_compare_sell_price","wb") as f:
    pickle.dump(USD_compare_sell_price,f)


#==============================================================================
#==============================================================================
#抓取患者人數

import pandas as pd
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
hii = pd.read_csv(url)
#把不需要的刪掉
data=hii.drop(columns=["UID","iso2","iso3","code3","FIPS","Admin2","Province_State","Country_Region","Lat","Long_","Combined_Key"]) #把不需要的刪掉列
data.loc['US_sum'] = data.apply(lambda x: x.sum()) # 增加一行相加的數
datatest=data.diff(axis=1) #進行反向累計，現在的US_sum是每日新增數量
#================================================================================
#改時間標
list =[]
for i in range(0,len(datatest.columns)):
    a = datetime.datetime.strptime(str(datatest.columns[i]), "%m/%d/%y").date()
    list.append(a) #因為不能直接對columns做修改，故另外先加在　list 中

datatest.columns = list

temptemp = datatest.loc["US_sum"] # 抓出US_sum

US_sum = temptemp.loc[USD_date]
US_informed = US_sum[0:-1].tolist()
US_informed.append(0)
#==============================================================================
#抓出需要的資料
import pickle
#dic = data2['US_sum'].tolist()
#dic.append(data2['US_sum'])
file= open('US_informed.pickle','wb')
pickle.dump(US_informed,file)
file.close()

#=========================================================================
#=========================================================================
#畫出外匯的圖
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from matplotlib.font_manager import FontProperties

#資料匯入
myfont = FontProperties(fname='D:/Programs/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/msjh.ttc')
'''
with open("USD_compare_buy_price.pickle","rb") as f:
    USD_compare_buy_price=pickle.load(f)
with open("USD_compare_sell_price.pickle","rb") as f:
    USD_sell_price=pickle.load(f)
with open ('US_sum.pickle','rb') as f:
    US_sum = pickle.load(f)
'''
#USD buy price圖片製作

fig, ax1 = plt.subplots(figsize=(30, 6))
plt.xlabel("date", fontsize=30, labelpad = 5) # x軸叫日期
plt.title("USD purchase price VS. COVID-19 comfirmed cases ratio",x=0.5, y=1.03,fontsize=20)
#USD buy price的線
ax1.plot(USD_compare_buy_price,'s-', color='r', alpha=0.75,label="USD buy price")
ax1.set_xticks(range(0, len(USD_date)))
ax1.set_xticklabels(USD_date,rotation = 45)
ax1.set_xlabel("date",fontsize=20) 
ax1.legend(loc=3)
#COVID-19的線
ax2 = ax1.twinx()
ax2.plot(US_informed,'s-',color = 'b',label="US confirmed")
ax2.set_ylabel("confirmed number",fontsize=20) 
#plt.ylabel("price", fontsize=30, labelpad = 10)
#plt.legend()
ax2.legend(loc=0)
fig.tight_layout()
plt.savefig("./US purchase price vs. COVID-19.jpg") #存圖
plt.show()
#===============================================================
#USD sell price圖片製作
fig, ax1 = plt.subplots(figsize=(30, 6))
plt.xlabel("date", fontsize=30, labelpad = 5) # x軸叫日期
plt.title("USD sell price VS. COVID-19 comfirmed cases ratio",x=0.5, y=1.03,fontsize=20)


ax1.plot(USD_compare_buy_price,'s-', color='g', alpha=0.75,label="USD sell price")
ax1.set_xticks(range(0, len(USD_date)))
ax1.set_xticklabels(USD_date,rotation = 45)
ax1.set_xlabel("date",fontsize=20) 
ax1.legend(loc=3)


ax2 = ax1.twinx()
ax2.plot(US_informed,'s-',color = 'b',label="US confirmed")
ax2.set_ylabel("confirmed number",fontsize=20) 

ax2.legend(loc=0)
fig.tight_layout()
plt.savefig("./US sell price vs. COVID-19.jpg") # 存圖
plt.show()




