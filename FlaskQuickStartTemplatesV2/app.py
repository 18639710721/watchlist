# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 22:02
# @Author  : listem
# @FileName: app.py
# @Software: PyCharm
"""

"""

from flask import Flask, render_template  # 生产视图函数对应的URL

# 实例化Flask类 创建一个程序对象app
app = Flask(__name__)

"""
使用路由装饰器来为这个函数绑定对应的 URL
触发这个函数获取返回值，并把返回值显示到浏览器窗口
    第一个参数是URL规则字符串 这里的/指的是根地址
"""

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies) # 通过关键字参数传入变量


# 定义一些虚拟数据
name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=7777,
        debug=True
    )
