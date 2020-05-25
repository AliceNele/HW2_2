# -*- coding: utf-8 -*-
"""
Created on Tue May 12 01:20:56 2020

@author: ASUS
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/<page>')
def index(page):
    return render_template(page +'.html')
if __name__ == '__main__':
    app.run()