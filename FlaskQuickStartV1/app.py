# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 22:02
# @Author  : listem
# @FileName: app.py
# @Software: PyCharm
"""

"""

from flask import Flask, url_for  # 生产视图函数对应的URL
from markupsafe import escape

# 实例化Flask类 创建一个程序对象app
app = Flask(__name__)

"""
使用路由装饰器来为这个函数绑定对应的 URL
触发这个函数获取返回值，并把返回值显示到浏览器窗口
    第一个参数是URL规则字符串 这里的/指的是根地址
"""


@app.route('/')
@app.route('/index')
@app.route('/home')
# 请求处理函数 视图函数（view function）
def hello():
    # return 'Welcome to My Watchlist!'
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


# 定义url中的变量
@app.route("/user/<name>")
def user_page(name):
    return f'User: {escape(name)}'  # 防范恶意代码 用escape对变量进行转义


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='greyli'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))  # 关键字参数作为查询字符串
    return 'Test page'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=7777,
        debug=True
    )
