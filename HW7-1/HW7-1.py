# -*- coding: utf-8 -*-
"""
Created on Mon May 25 01:34:01 2020

@author: Alice Cheng
"""
#==================================
'''
from flask import Flask, request
#from flask import render_template

app = Flask(__name__)

@app.route('/checkCreditCard',methods=['POST'])
def login():
    if request.method == 'POST':
        with open(name +".pkl",'rb') as f:
            account = pickle.load(f)
        balance = account.getBalance()
        return '餘額： ' + request.values['username'].balance
    return "<form method = 'post' action='/login'>" \
           "<input type='text' name='username' />" \ 
           "</br>" \
           "<button type='submit'>Submit</button>" \
           "</form>"
if __name__ == '__main__':
    app.run()
#=======================
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/checkCreditCard')
def login():
    return render_template('creditcard.html')
if __name__ == '__main__':
    app.run()
'''
#============================
from flask import Flask, request
from flask import render_template
import pickle
app = Flask(__name__)

@app.route('/checkCreditCard',methods=['POST'])
def login():
    if request.method == 'POST':
        with open('username' +".pkl",'rb') as f:
            account = pickle.load(f)
        balance = account.getBalance()
        return '餘額： ' + balance
    return render_template('creditcard.html')
    
if __name__ == '__main__':
    app.run()

'''
return  "<form method ='post' action='/login'>" \
           "<input type='text' name='username' />" \
            "</br>" \
           "<button type='submit'>Submit</button>" \
           "</form>"
'''


















