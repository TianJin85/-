# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    :  2020/3/13 10:06
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import Blueprint
from app.api.back import wechat


def create_back():
    bp_v1 = Blueprint('back', __name__)
    wechat.back.register(bp_v1)
    return bp_v1