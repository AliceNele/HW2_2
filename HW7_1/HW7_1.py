# -*- coding: utf-8 -*-
# @author: Alice Cheng

from flask import Flask, request
from flask import render_template
import os
import pickle
from CreditCardAccount import CreditCardAccount
app = Flask(__name__)

data_folder = "Data"
credit_data_folder = os.path.join(data_folder, "CreditCard")
if not os.path.exists(credit_data_folder):
    os.makedirs(credit_data_folder)

@app.route('/checkCreditCard', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        filename = request.form["username"] + ".pkl"
        filename = os.path.join(credit_data_folder, filename)
        with open(filename, "rb") as f:
            account = pickle.load(f)
        balance = account.getBalance()
        return '餘額： ' + str(balance)
    else:
        return render_template('creditcard.html')

if __name__ == '__main__':
    app.run()


