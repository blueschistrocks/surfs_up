#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:53:57 2022

@author: robertvanderweele
"""

from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'