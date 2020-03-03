# -*- encoding: utf-8 -*-
"""
@File    : __init__.py
@Time    :  2020/3/2 17:32
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import Blueprint
from app.api.view import wechat


def create_view():
    bp_v1 = Blueprint('view', __name__)
    wechat.wechat.register(bp_v1)
    return bp_v1