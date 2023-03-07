# -*- coding: utf-8 -*-
# @Time    : 2023/3/7 14:45
# @Author  : listem
# @FileName: test.py
# @Software: PyCharm

"""
生成和验证密码散列值的函数
"""

from werkzeug.security import generate_password_hash, check_password_hash

pw_hash = generate_password_hash('dog')
print(pw_hash)
print(check_password_hash(pw_hash, 'dog'))  # 验证散列值是否对应密码 dog
print(check_password_hash(pw_hash, 'cat'))
