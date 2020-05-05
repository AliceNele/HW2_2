# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:12:39 2020

@author: ASUS
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:01:08 2020

@author: ASUS
"""
import pickle
import pandas as pd
#找出國家
url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
res = pd.read_html(url)
data= res[0].iloc[:,0:1]
#data_country.to_pickle('country.pickle')
#country = pd.read_pickle("country.pickle")

data.columns = ["幣別"]

data.to_excel("test.xlsx")
#==============================================================================
country_name = ["USD","HKD","JPY","CNY"]
                #美國、港幣、日圓、人民幣
#找出資料，抓近三個月的
import pandas as pd
import pickle
import requests
import os 
from io import StringIO
os.getcwd()


for i in range(0,len(country_name)):
    folder = "./data/" +country_name[i]
    if not os.path.exists(folder):
        os.makedirs(folder)
    url = "https://rate.bot.com.tw/xrt/quote/ltm/" + country_name[i] + "/"
    r = requests.get(url)
    r.encoding='utf-8-sig'
    hello = pd.read_html(StringIO(r.text),encoding='utf-8-sig')
    
    data = hello[0].iloc[:,0:6]
    data.columns = [u"掛牌日期",u"幣別", u"現金買入",u"現金買入",u"即期買入",u"即期賣出"]
    
    data.to_csv(os.path.join(folder,(str(country_name[i]))+".csv"),encoding="utf-8-sig")
    #data = data.to_pickle(country[0]+".pickle") 

    #f = open(str(country_name[i])+".pickle","wb")
    #pickle.dump(data,f)
    #f.close()
    #with open(str(country_name[i])+".pickle","rb") as f:
   #     pickle.load(f)
#======================================================
#讀取資料
import pandas as pd
data=pd.read_csv("./data/USD/USD.csv")
USD_buy = data['即期買入'].tolist()
USD_sell = data['即期賣出'].tolist()
data=pd.read_csv("./data/HKD/HKD.csv")
HKD_buy = data['即期買入'].tolist()
HKD_sell = data['即期賣出'].tolist() 
data=pd.read_csv("./data/JPY/JPY.csv")
JPY_buy = data['即期買入'].tolist()  
JPY_sell = data['即期賣出'].tolist()
data=pd.read_csv("./data/CNY/CNY.csv")
CNY_buy = data['即期買入'].tolist()
CNY_sell = data['即期賣出'].tolist()
#到此，匯率資料抓取完畢
#=================================================================
USD_price = []
for i in range(1,len(USD_buy)):
    a = USD_buy[i] - USD_buy[i-1]
    USD_price.append(a)
#===============================================================================
import pandas as pd
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
hi = pd.read_csv(url)
hi1=hi.drop(columns=["Lat","Long"]) #把不需要的刪掉列
#hi1[266]=hi1[0:1].sum(0)#上下加總
#h1["china_sum"]=df[49:81].sum(0)#上下加總

indicator = hi1[49:81].tolist(0)

#hi2 = hi1.T

#===========================================
#畫出外匯的圖
import matplotlib.pyplot as plt

import pickle
import pandas as pd

with open(str(country_name[i])+".pickle","rb") as f:
        pickle.load(f)

#測試====================================
import pandas as pd
url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"

res=pd.read_html(url)
data1=res[0].iloc[:,0:2]
data1.columns=["幣別","現金買入"]
data1.to_excel("testdata.xlsx")



import pandas as pd
import os 
os.getcwd()
url = "https://rate.bot.com.tw/xrt/quote/ltm/" + "USD" + "/"
hello = pd.read_html(url)
data = hello[0].iloc[:,0:6]
data.columns = [u"掛牌日期",u"幣別", u"現金買入",u"現金買入",u"即期買入",u"即期賣出"]

with open('writedFile.csv','w') as f:
    writeCsv = csv.writer(f)
    writeCsv.writerow(headers)
    writeCsv.writerows(rows)


data.to_csv("USD.csv")


