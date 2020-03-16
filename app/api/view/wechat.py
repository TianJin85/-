# -*- encoding: utf-8 -*-
"""
@File    : wechat.py
@Time    :  2020/3/2 17:27
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import base64
import json
import os

import requests
from lin.redprint import Redprint

from flask import render_template, redirect, request, jsonify, url_for, Response

from app.config.secure import WxAppidSecretSecure
from app.controller.save import Save
from app.models.message import Message
from app.models.selection import Selection
from app.models.user import User
from app.validators.love_forms import MessageForm

wechat = Redprint("wechat")

wechat_secure = WxAppidSecretSecure()


@wechat.route("/", methods=['GET'])
def test():
    APPID = "wxb10a1f7d311d8f9b"
    REDIRECT_URI = "http://www.anshun520.com/view/wechat/personal"
    SCOPE = "snsapi_userinfo "
    source_url = 'https://open.weixin.qq.com/connect/oauth2/authorize' \
                 + '?appid={APPID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={SCOPE}' \
                 + '#wechat_redirect'
    # REDIRECT_URI = quote(REDIRECT_URI, 'utf-8')
    # url = source_url.format(APPID=APPID, REDIRECT_URI=REDIRECT_URI, SCOPE=SCOPE)
    url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxb10a1f7d311d8f9b&redirect_uri=http://www.anshun520.com/view/wechat/index&response_type=code&scope=snsapi_userinfo&state=123&connect_redirect=1#wechat_redirect"

    return redirect(url)


@wechat.route("/index/<userid>", methods=[ "GET"])
@wechat.route("/index", methods=["GET"])
def index(userid=None):
    userinfo = {"userid": userid, "messid": None}
    code = request.args.get('code')
    if code:
        source_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?'\
            +'appid={APPID}&secret={APPSECRET}&code={CODE}&grant_type=authorization_code'
        access_token_url = source_url.format(APPID=wechat_secure.appdi, APPSECRET=wechat_secure.secret, CODE=code)
        resp = requests.get(access_token_url)
        if resp.ok:
            data = eval(resp.text) # 将字符串转为字典
            openid = data['openid']
            access_token = data["access_token"]
            info_url = " https://api.weixin.qq.com/sns/userinfo?access_token={ACCESS_TOKEN}&openid={OPENID}&lang=zh_CN"
            resp_user = requests.get(info_url.format(ACCESS_TOKEN=access_token, OPENID=openid))
            if resp_user.ok:
                result = eval(resp_user.text)

                user = User.add_openid(openid=openid, headimgurl=result["headimgurl"])    # 查询数据数据不存在就储存数据
                if user:
                    userid = User.get_user_id(openid=openid)
                    messid = Message.get_messid(uid=userid)
                    userinfo["messid"] = messid
                    userinfo["userid"] = userid
        else:
            return "登录失败"
    #
    # data = Message.get_index()          # 查询数据库
    #
    # for mess, select in data:
    #     mess_dic = mess.__dict__
    #
    #     delattr(mess, "cardid")
    #
    #     setattr(mess, "images", eval(mess_dic["images"])[0])
    #     setattr(mess, "userinfo", userinfo)
    #     mess._fields.append("userinfo")
    # result = jsonify(data)
    result = []
    data = Message.get_mess_all()

    for mess in data:
        mess_dict = mess.__dict__
        setattr(mess, "images", eval(mess_dict["images"])[0])
        setattr(mess, "userinfo", userinfo)
        mess._fields.append("userinfo")
        result.append(mess.__dict__)

    return render_template("index.html", result=result)


@wechat.route("/integral/<userid>", methods=[ "GET"])
@wechat.route("/integral", methods=['GET'])
def integral(userid=None):
    mess = Message.get_messid(uid=userid)
    print(mess)

    return render_template("integral.html", userid=userid)


@wechat.route("/activity/<userid>", methods=["POST", "GET"])
@wechat.route("/activity", methods=['GET'])
def activity(userid=None):

    return render_template("activity.html", userid=userid)


@wechat.route("/activity_details/<userid>", methods=["POST", "GET"])
@wechat.route("/activity_details", methods=["GET"])
def activity_details(userid=None):
    return render_template("activity_details.html")


@wechat.route("/consumption/<userid>", methods=["POST", "GET"])
@wechat.route("/consumption", methods=["GET"])
def consumption(userid):
    return render_template("consumption.html")


@wechat.route("/enroll/<userid>", methods=["POST", "GET"])
@wechat.route("/enroll", methods=["POST", "GET"])
def enroll(userid=None):
    form = MessageForm(request.form)

    if request.method == "POST":
        if form.validate():
            try:
                result = request.form.to_dict()
                imgpath = Save(result=result).get_data()        # 保存图片获取地址
                cardidinfo = Message.set_cardid(result["cardid"])
                mess_data = {
                    "uid": result["userid"],
                    "username": result["username"],
                    "census": result["census"],
                    "cardid": result["cardid"],
                    "stature": result["stature"],
                    "weight": result["weight"],
                    "wechat": result["wechat"],
                    "qq": result["qq"],
                    "school": result["school"],
                    "education": result["education"],
                    "workunit": result["workunit"],
                    "occupation": result["occupation"],
                    "profession": result["profession"],
                    "monthly": result["monthly"],
                    "member": result["member"],
                    "housing": result["housing"],
                    "rest": result["rest"],
                    "vehicle": result["vehicle"],
                    "marriage": result["marriage"],
                    "phone": result["phone"],
                    "images": imgpath,
                    "sex": cardidinfo["sex"],
                    "age": cardidinfo["age"]
                }

                Message.add_message(**mess_data)
                mess_id = Message.get_messid(uid=result["userid"])
                select_data = {"mid": mess_id,
                        "marriage": result["marriage"],
                        "age": result["age"],
                        "stature": result["ze_stature"],
                        "weight": result["ze_weight"],
                        "monthly": result["ze_monthly"],
                        "housing": result["ze_housing"],
                        "vehicle": result["ze_vehicle"],
                        "children": result["ze_housing"],
                        "census": result["ze_census"],
                        "pests": result["ze_pests"]}
                Selection.add_selection(**select_data)
                return jsonify({"data": "数据提交成功", "status": 200})
            except os.error as e:
                return jsonify({"errors": e, "status": 500})
        else:
            error_data = ""
            for items in form.errors.values():
                for item in items:
                    error_data+=item+"\n"

            return jsonify({"errors": error_data, "status": 300})

    return render_template("enroll.html", userid=userid)


@wechat.route("/vip_hyfw/<userid>", methods=["GET"])
@wechat.route("/vip_hyfw")
def vip_hyfw(userid=None):
    return render_template("vip_hyfw.html", userid)


@wechat.route("/my_balance/<userid>", methods=["GET"])
@wechat.route("/my_balance")
def my_balance(userid=None):

    return render_template("my_balance.html", userid=userid)



@wechat.route("/upenroll/<userid>", methods=["GET"])
@wechat.route(("/upenroll"))
def upenroll(userid=None):

    return render_template("upenroll.html", userid=userid)


@wechat.route("/message/<userid>", methods=["GET"])
@wechat.route("/message", methods=["GET"])
def message(userid=None):

    return render_template("message.html", userid=userid)


@wechat.route("/message_details/<userid>", methods=["GET"])
@wechat.route("/message_details", methods=["GET"])
def message_details(userid=None):
    User.add_vip(userid)
    return render_template("message_details.html")


@wechat.route("/order/<userid>", methods=["GET"])
@wechat.route("/order", methods=["GET"])
def order(userid=None):
    return render_template("order.html")


@wechat.route("/order_details/<userid>", methods=["GET"])
@wechat.route("/order_details", methods=["GET"])
def order_details(userid=None):
    return render_template("order_details.html", userid=userid)


@wechat.route("/personal/<userid>", methods=["GET"])
@wechat.route("/personal", methods=["GET"])
def personal(userid=None):
    mess_data =Message.get_message(userid)
    mess_data["userid"] = userid
    return render_template("personal.html", mess_data=mess_data)

@wechat.route("/personal_details/<userid>", methods=["GET"])
@wechat.route("/personal_details", methods=["GET"])
def personal_details(userid=None):

    return render_template("personal_details.html")


@wechat.route("/recharge/<userid>", methods=["GET"])
@wechat.route("/recharge", methods=["GET"])
def recharge(userid=None):
    return render_template("recharge.html")


@wechat.route("/recharge_vip/<userid>", methods=["GET"])
@wechat.route("/recharge_vip", methods=["GET"])
def recharge_vip(userid=None):
    return render_template("Recharge_vip.html")


@wechat.route("/search_criteria/<userid>", methods=["GET"])
@wechat.route("/search_criteria", methods=["GET"])
def search_criteria(userid=None):

    return render_template("search_criteria.html")


@wechat.route("/search_result/<userid>", methods=["GET"])
@wechat.route("/search_result", methods=["GET"])
def search_result(userid=None):
    return render_template("search_result.html", userid)


@wechat.route("/see_qq/<userid>", methods=["POST", "GET"])
@wechat.route("/see_qq", methods=["GET"])
def see_qq(userid=None):

    return render_template("see_qq.html")




@wechat.route("/messinfo/<userid>", methods=["POST", "GET"])
@wechat.route("/messinfo", methods=["GET", "POST"])
def messinfo(userid=None):
    if request.method == "POST":
        userid = request.form["userid"]
        data = Message.get_unenroll(userid)
        return jsonify(data)
    data = Message.get_unenroll(userid)
    return jsonify(data)

@wechat.route("/indexinfo/<userid>", methods=["POST", "GET"])
@wechat.route("/indexinfo", methods=["GET", "POST"])
def indexinfo(userid=None):

    data = Message.get_index()

    for mess, select in data:

        mess_dic = mess.__dict__
        # select_dic = select.__dict__

        # result = Message.set_cardid(mess.cardid)
        #
        # setattr(mess, "sex", result["sex"])
        # setattr(mess, "age", result["age"])
        delattr(mess, "cardid")
        # mess._fields.append("sex")
        # mess._fields.append("age")
        setattr(mess, "images", eval(mess_dic["images"])[0])

    return jsonify(data)
