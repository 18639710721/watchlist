# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 11:15
# @Author  : listem
# @FileName: app.py.py
# @Software: PyCharm

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'


if __name__ == '__main__':
    app.run()
