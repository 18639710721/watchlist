"""
模型类
"""
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from watchlist import db


# 添加UserMinxin让User类继承判断认证状态的属性和方法
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字
    username = db.Column(db.String())  # 用户名
    password_hash = db.Column(db.String(128))  # 密码散列值

    # 用来设置密码发方法, 接受密码作为参数
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # 用于验证密码发方法 接受密码作为参数
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))
