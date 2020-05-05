# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:35:22 2020

@author: ASUS
"""

import re # 再尋找 html 很好用

#ex1
pattern1 = "cat"
pattern2 = "dog"
string = "apple bird cat"
#print(pattern1 in string)
#print(pattern2 in string)

#ex2
result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string)
print(result1)
print(result2)

#多種可能
string1 = "A ru to B"
string2 = "A ran to B"
pattern = r'r[au]n'
result1 = re.search(pattern,string1)
result2 = re.search(pattern,string2)
print(result1)
print(result2)

##自己嘗試可能
string1 = "A ruqn to B"
string2 = "A raon to B"
pattern = r'r[auq][qio]n' # 一個[]一個格子
result1 = re.search(pattern,string1)
result2 = re.search(pattern,string2)
print(result1)
print(result2)

#更多可能-1
string1 = "A run to B"
string2 = "A rUn to B"
pattern = r'r[a-z]n' # 一個[]一個格子
result1 = re.search(pattern,string1)
result2 = re.search(pattern,string2)
print(result1)
print(result2)

#自己嘗試
string1 = "A run to B"
string2 = "A rUn to B"
pattern = r'r[A-z]n' # 我可以從大寫測到小寫
#pattern = r'r[A-Za-z]n'
#pattern = r'r[0-9]n'
result1 = re.search(pattern,string1)
result2 = re.search(pattern,string2)
print(result1)
print(result2)

#更多可能-2
string1 = "A r3n to B"
string2 = "A rUn to B"
#pattern = r'r[A-z]n' # 我可以從大寫測到小寫
#pattern = r'r[A-Za-z]n'
#pattern = r'r[0-9]n'
pattern = r'r[A-Z0-9]n'
result1 = re.search(pattern,string1)
result2 = re.search(pattern,string2)
print(result1)
print(result2)

#其他表示法-1

string = "run r3n"
pattern1 = r'r\dn' # 測數字0-9
pattern2 = r'r\Dn'

result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string)
print(result1)
print(result2)

##
#\w = [a-zA-Z0-9_] 
string = "r_n \tn"
pattern1 = r'r\wn' # 能測字母，也有底線喔！！
pattern2 = r'r\Wn'

result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string)
print(result1)
print(result2)

##
string = "run \tn"
pattern1 = r'r\sn' # 測[\t\n\r]
pattern2 = r'r\Sn'

result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string)
print(result1)
print(result2)

#句首/句尾/任意字元
string1 = "A run to B"
string2 = "A ran to B"
string3 = "nI w"
pattern1 = r"^A"
pattern2 = r"B$"
pattern3 = r"r.n"
result1 = re.search(pattern1,string1)
result2 = re.search(pattern2,string2)
result3 = re.search(pattern3,string2)
result4 = re.search(pattern3,string3)

print(result1) # <re.Match object; span=(0, 1), match='A'>
print(result2) # <re.Match object; span=(9, 10), match='B'>
print(result3) # <re.Match object; span=(2, 5), match='ran'>
print(result4)

#
#*：0次或多次
print(re.search(r"ab*","a"))
print(re.search(r"ab*","abbbbbbbbb"))
#+：1或多次
print(re.search(r"ab+","a"))
#可有可無
result1 = re.search(r"NTHU(QF)?","NTHU")

print(result1) # <re.Match object; span=(0, 4), match='NTHU'>

#有換行，flags = re.M
string = '''
A run to B.
I run to B.
'''
print(re.search(r"^I",string))               #None
print(re.search(r"^I",string,flags = re.M))  #<re.Match object; span=(13, 14), match='I'>

#出現指定次數
print(re.search(r"ab{2,10}","a"))           # None
print(re.search(r"ab{2,10}","abbbbbbbbbb")) # <re.Match object; span=(0, 11), match='abbbbbbbbbb'>

#group
result = re.search(r'(\d+), Date: (.+)',"ID: 123456, Date: 2020/04/21")
print(result.group())
print(result.group(1))
print(result.group(2))

##幫 group 取名
result = re.search(r'(?P<id>\d+), Date: (?P<date>.+)',"ID: 123456, Date: 2020/04/21")
print(result.group())
print(result.group("id"))
print(result.group("date"))

# findall
string = "run ran r3n run"
result = re.findall(r'(run|ran)',string)
print(result)    #['run', 'ran', 'run']

#sub替換
string = "run ran r3n"
print(re.search(r'r[0-9]n',"run",string))
#split
string = "run,ran;r3n/r8n"
print(re.split(r'[,;/]',string)) #['run', 'ran', 'r3n', 'r8n']
#compile
result = re.search(r'(?P<id>\d+), Date: (?P<date>.+)',"ID: 123456, Date: 2020/04/21")
print(result)
##與下面比較
compiled_re = re.compile(r'(?P<id>\d+), Date: (?P<date>.+)')
result = compiled_re.search("ID: 123456, Date: 2020/04/21")
print(result)

# match
string = 'run ran r3n'
print(re.match(r"r.n r.n",string))  #<re.Match object; span=(0, 7), match='run ran'>
print(re.match(r"ran r3n",string))  #None
print(re.match(r"r.n r.n$",string)) #None







