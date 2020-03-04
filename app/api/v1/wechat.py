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


from app.nosql.resdb import RedisDB
from app.config.secure import WxAppidSecretSecure, RedisSecure
from app.models.love import Love_ctivity, Love_message, Love_user, Love_payment

wechat_api = Redprint("wechat")


wechat = WxAppidSecretSecure()
res = RedisSecure()


@wechat_api.route("/get_token", methods=["GET"])
def get_token():

    result = requests.get(wechat.url.format("token"), params={"grant_type": "client_credential",\
                                           "appid": wechat.appdi, "secret": wechat.secret})
    result = eval(result.text)
    if "errcode" not in result:
        with RedisDB(host=res.host, port=res.port, db=res.db) as conn:
            conn.set("access_token", result["access_token"])

    return jsonify(result)


@wechat_api.route("/get_user", methods=["GET"])
def get_user():
    open_id = []

    with RedisDB(host=res.host, port=res.port, db=res.db) as conn:
        token = conn.get("access_token")

    params = {"access_token": str(token, encoding="utf8"), "next_openid": None}

    for item in range(3):
        result = requests.get(wechat.url.format("user/get"), params=params)
        result = eval(result.text)
        next_openid = result["next_openid"]

        if "data" in result:
            openid_list = result["data"]["openid"]

        if next_openid is not "":
            for item in openid_list:
                open_id.append(item)
            params["next_openid"] = result["next_openid"]
        else:
            break

    for id in open_id:

        resp = requests.get(wechat.url.format("user/info"), params={"access_token": str(token, encoding="utf8"),\
                                                                   "openid": id} )


        print(resp.text)

    return jsonify({"opne_id": open_id})
