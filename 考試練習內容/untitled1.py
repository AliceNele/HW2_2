# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:06:10 2020

@author: ASUS
"""


#Lab6
from flask import Flask, request,render_template, redirect,url_for,flash

app = Flask(__name__)

def login_check(username,password):
    if username == 'admin' and  password == '1234':
        return True
    else:
        return False

@app.route('')
@app.route('/loginurl',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('Hello' ,username=request.form.get('username')))
    
    return render_template('login.html')
@app.route('hello/')

