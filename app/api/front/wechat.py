# -*- encoding: utf-8 -*-
"""
@File    : wechat.py
@Time    :  2020/3/13 10:09
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import request, jsonify
from lin.redprint import Redprint

from app.models.message import Message

front = Redprint("wechat")


@front.route("/search_sex", methods=["GET"])
def search_sex():
    sex = request.args["sex"]
    if sex:
        mess = Message.get_sex(sex=sex)
    return jsonify(mess)


@front.route("/search_id", methods=["GET"])
def search_id():
    result = None
    uid = request.args["uid"]
    if uid:
        result = Message.get_unenroll(uid=uid)
<<<<<<< HEAD
        try:
            delattr(result[0], "cardid")  # 删除属性
        except TypeError as e:
            print(e)
=======

        delattr(result[0], "cardid")  # 删除属性
>>>>>>> origin/master

    return jsonify(result)


@front.route("/search_criteria", methods=["GET"])
def search_search_criteria():

    return request.args.to_dict()