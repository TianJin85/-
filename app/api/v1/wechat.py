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
import redis


from app.config.secure import WxAppidSecretSecure, RedisSecure
from app.nosql.resdb import RedisDB

wechat_api = Redprint("wechat")


wechat = WxAppidSecretSecure()
res = RedisSecure()


@wechat_api.route("/get_token", methods=["GET"])
def get_token():

    result = requests.get(wechat.url.format("token"), params={"grant_type": "client_credential",\
                                           "appid": wechat.appdi, "secret": wechat.secret})
    print(result.text)
    with RedisDB(host=res.host, port=res.port, db=res.db) as conn:
        conn.set("access_token", eval(result.text)["access_token"])

    return result.json()


@wechat_api.route("/get_user", methods=["GET"])
def get_user():
    user_list = []
    with RedisDB(host=res.host, port=res.port, db=res.db) as conn:
        token = conn.get("access_token")

    while True:
        result = requests.get(wechat.url.format("user/get"), \
                              params={"access_token": str(token, encoding="utf8"), "next_openid": None})
        # next_openid = eval(result.text)["next_openid"]
        print(result.text)
        break

    return result.json()
