# -*- encoding: utf-8 -*-
"""
@File    : personal.py
@Time    :  2020/3/13 17:15
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import request, jsonify
from lin.exception import Success, ParameterException, UnknownException
from lin.redprint import Redprint

from app.models.message import Message
from app.models.search_message import Serch_message
from app.models.user import User

pers_api = Redprint("personal")


@pers_api.route("/personal_details", methods=["GET"])
def personal_details():
    result = None
    uid = request.args["uid"]
    if uid:
        result = Message.get_unenroll(uid=uid)

        delattr(result[0], "cardid")  # 删除属性

    return jsonify(result)


@pers_api.route("/collect", methods=["GET"])
def collect():
    uid = request.args["id"]
    cid = request.args["cid"]

    if uid and cid:

        if User().collect(id=uid, cid=cid):
            return Success(msg="收藏成功")
        else:
            return UnknownException()
    else:
        return ParameterException()


@pers_api.route("/search_wx", methods=["GET"])
def search_wx():
    id = request.args["id"]
    uid = request.args["uid"]

    if id !=uid:
        if Serch_message.search_wx(id, uid):

            return Success()
    return Success()


@pers_api.route("/search_qq", methods=["GET"])
def search_qq():
    id = request.args["id"]
    uid = request.args["uid"]

    if id != uid:
        if Serch_message.search_qq(id, uid):
            return Success()
    return Success()


@pers_api.route("/search_phone", methods=["GET"])
def search_phone():
    id = request.args["id"]
    uid = request.args["uid"]

    if id != uid:
        if Serch_message.search_phone(id, uid):
            return Success()
    return Success()


@pers_api.route("/qq_list", methods=["GET"])
def qq_list():
    id = request.args["id"]
    result = Serch_message.qq_list(id=id)
    if result:
        return jsonify(result)
    return Success(msg="暂时没有人查看您的信息")


@pers_api.route("/wx_list", methods=["GET"])
def wx_list():
    id = request.args["id"]
    result = Serch_message.wx_list(id=id)
    if result:
        return jsonify(result)
    return Success(msg="暂时没有人查看您的信息")


@pers_api.route("/phone_list", methods=["GET"])
def phone_list():
    id = request.args["id"]
    result = Serch_message.phone_list(id=id)
    if result:
        return jsonify(result)
    return Success(msg="暂时没有人查看您的信息")


@pers_api.route("my_collect", methods=["GET"])
def my_collect():
    id = request.args["id"]
    result = User.my_collect(id=id)
    if result:
        return jsonify(len(eval(result)))
    else:
        return Success()