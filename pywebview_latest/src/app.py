# -*- coding: utf-8 -*-
"""
    Calculator
    ~~~~~~~~~~~~~~

    A simple Calculator made by Flask and jQuery.

    :copyright: (c) 2015 by Grey li.
    :license: MIT, see LICENSE for more details.
"""
import re
from flask import Flask, jsonify, render_template, request

import webview
import sys
import threading

app = Flask(__name__)


@app.route('/_calculate')
def calculate():
    a = request.args.get('number1', '0')
    operator = request.args.get('operator', '+')
    b = request.args.get('number2', '0')
    m = re.match('-?\d+', a)
    n = re.match('-?\d+', b)
    if m is None or n is None or operator not in '+-*/':
        return jsonify(result='I Catch a BUG!')
    if operator == '/':
        result = eval(a + operator + str(float(b)))
    else:
        result = eval(a + operator + b)
    return jsonify(result=result)


@app.route('/')
def index():
    return render_template('index.html')

def start_server():
    app.run(host="0.0.0.0",port="80");
 
if __name__ == '__main__':
    """  https://github.com/r0x0r/pywebview/blob/master/examples/http_server.py
    """
 
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
 
    webview.create_window("Calculator", "http://127.0.0.1:80/")
    webview.toggle_fullscreen()
 
    sys.exit()