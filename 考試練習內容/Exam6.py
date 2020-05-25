# -*- coding: utf-8 -*-
"""
Created on Tue May 12 02:00:49 2020

@author: ASUS
"""

from flask import Flask, request,render_template,redirect,url_for,flash
app = Flask(__name__)

def login_check(username,password):
    if username == 'admin' and password == '1234':
        return True
    else:
        return False
@app.route('/hello/<username>')
def hello(username):
    return render_template('variable1.html',name=username)

@app.route('loginurl',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if login_check(request.form['username'],request.form['password']):
            return redirect(url_for('hello',username=request.form.get('username')))
        else:
            return "<h1>帳號或密碼錯誤</h1>"
    return render_template('UserLogin.html')

if __name__ == '__main__':
    app.run()