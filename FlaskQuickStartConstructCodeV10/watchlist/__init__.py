# -*- coding: utf-8 -*-
# @Time    : 2023/3/7 18:38
# @Author  : listem
# @FileName: __init__.py.py
# @Software: PyCharm

"""
coverage run --source=watchlist test_watchlist.py
coverage html 生成

"""
import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

# 实例化Flask类 创建一个程序对象app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)

# 初始化Flask-Login
login_manager = LoginManager(app)  # 实例化扩展类
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数 接受用户ID作为参数
    from watchlist.models import  User
    user = User.query.get(int(user_id))  # 用ID作为User模型的主键查询对应的用户
    return user  # 返回用户对象


@app.context_processor
def inject_user():  # 函数名可以随意修改
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)  # 需要返回字典, 等同于 return {'user': user}


# 为了避免循环依赖
from watchlist import views, error, commands
