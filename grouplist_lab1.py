# -*- coding: utf-8 -*-
"""
Created on Tue May 12 02:17:18 2020

@author: ASUS
"""

import pandas as pd
grouplist = pd.read_csv("groupList.csv")

team = grouplist['Team'].tolist()
element = list(set(team))
freq = []
for i in element:
    freq.append(team.count(i))

single = []
for i in range(0,len(freq)):
    if freq[i] == 1:
        idx = team.index(element[i])
        single.append(grouplist['Name'][idx])
        
print(single)