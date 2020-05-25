# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:02:38 2020

@author: ASUS
"""
import pandas as pd
import requests
import os 
from io import StringIO
import urllib.parse





#=================================
a =str(input("請輸入書名："))

#reload(sys)                      # reload 才能调用 setdefaultencoding 方法  
#sys.setdefaultencoding('utf-8')
blank = " "
comma = ","
explatation = "!"
if blank in a:
    a.replace(blank, "+")

if comma in a:
    a.replace(comma, "%2C")

if explatation in a:
    a.replace(explatation, "%21")

a = input("請輸入書名：")
b = urllib.parse.quote(a) 
link = ("http://www.nthubook.com.tw/index.php?pa=book_list&keyword="+b+"&x=0&y=0")

link2 = urllib.request.urlopen(link)

data = pd.read_html(link2)

data_book = data[3]
c = data_book.drop('Unnamed: 5', axis=1)
