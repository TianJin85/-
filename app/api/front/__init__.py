# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    :  2020/3/13 10:07
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import Blueprint
from app.api.front import wechat


def create_front():
    bp_v1 = Blueprint('front', __name__)
    wechat.front.register(bp_v1)
    from .personal import pers_api
    pers_api.register(bp_v1)
    return bp_v1