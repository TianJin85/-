# -*- encoding: utf-8 -*-
"""
@File    : wechat.py
@Time    :  2020/3/2 17:27
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.redprint import Redprint

from flask import render_template
wechat = Redprint("wechat")


@wechat.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@wechat.route("/integral", methods=['GET'])
def integral():
    return render_template("integral.html")


@wechat.route("/activity", methods=['GET'])
def activity():
    return render_template("activity.html")


@wechat.route("/activity_details", methods=["GET"])
def activity_details():
    return render_template("activity_details.html")


@wechat.route("/consumption", methods=["GET"])
def consumption():
    return render_template("consumption.html")


@wechat.route("/enroll", methods=["GET"])
def enroll():
    return render_template("enroll.html")


@wechat.route("/message", methods=["GET"])
def message():
    return render_template("message.html")


@wechat.route("/message_details", methods=["GET"])
def message_details():
    return render_template("message_details.html")


@wechat.route("/order", methods=["GET"])
def order():
    return render_template("order.html")


@wechat.route("/order_details", methods=["GET"])
def order_details():
    return render_template("order_details.html")


@wechat.route("/personal", methods=["GET"])
def personal():
    return render_template("personal.html")


@wechat.route("/personal_details", methods=["GET"])
def personal_details():
    return render_template("personal_details.html")


@wechat.route("/recharge", methods=["GET"])
def recharge():
    return render_template("recharge.html")


@wechat.route("/recharge_vip", methods=["GET"])
def recharge_vip():
    return render_template("Recharge_vip.html")


@wechat.route("/search_criteria", methods=["GET"])
def search_criteria():
    return render_template("search_criteria.html")


@wechat.route("/search_result", methods=["GET"])
def search_result():
    return render_template("search_result.html")


@wechat.route("/see_qq", methods=["GET"])
def see_qq():
    return render_template("see_qq.html")