# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:49:55 2020

@author: ASUS
"""
'''
from flask import Flask
app = Flask(__name__) #__name__: 目前執行模組

@app.route("/") # 路徑 http://127.0.0.1:5000/
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/QF") # 路徑 http://127.0.0.1:5000/QF
def hello1():
    return "Hello QF!"

#以路徑來區分

if __name__ == "__main__": #如果是主程式
    app.run()

#===========================================
from flask import Flask
app = Flask(__name__) #__name__: 目前執行模組

@app.route("/") # 路徑 http://127.0.0.1:5000/
def hello():
    return "<h1><i>Hello World!<i></h1>"

if __name__ == "__main__": #如果是主程式
    app.run(host = '127.0.0.1',port = 8080)

#====================================================
from flask import Flask
app = Flask(__name__) 

@app.route("/") # 路徑 http://127.0.0.1:5000/
def hello():
    return "<h1><i>Hello World!<i></h1>"

@app.route("/hello/<name>")
def hello_name(name):
    return "<h1>Hello ,%s !</h1>" % name

if __name__ == "__main__": 
    app.run(host = '127.0.0.1',port = 8080)
    

#===================================================
#傳多變數
from flask import Flask
app = Flask(__name__) 

@app.route("/") # 路徑 http://127.0.0.1:5000/
def hello():
    return "<h1><i>Hello World!<i></h1>"

@app.route("/hello/<name>/<surname>") # 傳入兩個參數
def hello_name(name,surname):
    return "<h1>Hello ,{} {}</h1>".format(name,surname)

if __name__ == "__main__": 
    app.run(host = '127.0.0.1',port = 8080)



#===================================================
#傳變數
from flask import Flask,request
app = Flask(__name__) 

@app.route("/") # 路徑 http://127.0.0.1:5000/
def hello():
    return "<h1><i>Hello World!<i></h1>"

@app.route("/hello/") 
def hello_name():
    name = request.args.get("name")
    surname = request.args.get("surname")
    return "<h1>Hello ,{} {}</h1>".format(name,surname)

if __name__ == "__main__": 
    app.run(host = '127.0.0.1',port = 8080)
 
#===================================================
#打開模板
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()

#=========================================
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/para/<user>')
def index():
    return render_template('varible.html',name = user)

if __name__ == '__main__':
    app.run()

#========================================
#模板+多參數
from flask import Flask,request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    input_name = request.args.get("name")
    input_id = request.args.get("id")
    
    user_info = {
            "name": input_name,
            "id":input_id
            }
    return render_template('varible2.html',**user_info)

if __name__ == '__main__':
    app.run()

#========================================
from flask import Flask, request
app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return 'Hello' + request.values['username']
    
    return "<form method='post'    action='/login'>"\ # 用甚麼方法，向哪個連結傳送
           "<input type = 'text' name = 'username' />"\
           "</br>" \ #換行
           "<button type = 'submit'> Submit</button>" \
           "</form>"
if __name__ == '__main__':
    app.run()
'''
#===========================================
#重新導向(有成功)
from flask import Flask, request,render_template,redirect,url_for
app = Flask(__name__)

@app.route('/loginurl',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('hello',username=request.form.get('username')))
    
    return render_template('login.html')

@app.route('/hello/<username>')
def hello():
    if request.method == 'POST':
        return render_template('variable1.html',name=username)
       
if __name__ == '__main__':
    app.run()









