# -*- encoding: utf-8 -*-
"""
@File    : wechat.py
@Time    :  2020/2/24 16:25
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import requests
from flask import jsonify
from lin.redprint import Redprint


from app.config.secure import WxAppidSecretSecure

wechat_api = Redprint("wechat")


@wechat_api.route("/get_token", methods=["GET"])
def get_token():
    wechat = WxAppidSecretSecure()
    res = requests.get(wechat.url, params={"grant_type": "client_credential",\
                                           "appid": wechat.appdi, "secret": wechat.secret})

    return res.json()
