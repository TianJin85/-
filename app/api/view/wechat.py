# -*- encoding: utf-8 -*-
"""
@File    : wechat.py
@Time    :  2020/3/2 17:27
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import requests
from lin.redprint import Redprint

from flask import render_template, redirect, request, jsonify

from app.config.secure import WxAppidSecretSecure
from app.models.love import Love_user

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


@wechat.route("/index", methods=["GET"])
def index():
    code = request.args.get('code')
    source_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?'\
        +'appid={APPID}&secret={APPSECRET}&code={CODE}&grant_type=authorization_code'
    access_token_url = source_url.format(APPID=wechat_secure.appdi, APPSECRET=wechat_secure.secret, CODE=code)
    resp = requests.get(access_token_url)
    data = eval(resp.text) # 将字符串转为字典
    print(data)
    access_token = data['access_token']
    openid = data['openid']

    source_url = 'https://api.weixin.qq.com/sns/userinfo' \
                 + '?access_token={ACCESS_TOKEN}&openid={OPENID}&lang=zh_CN'
    useinfo_url = source_url.format(ACCESS_TOKEN=access_token, OPENID=openid)
    resp = requests.get(useinfo_url)
    data = eval(resp.text)
    print(data)
    userinfo = {
        'nickname': data['nickname'],
        'sex': data['sex'],
        'province': data['province'],
        'city': data['city'],
        'country': data['country'],
        'headimgurl': data['headimgurl']
    }
    return render_template("index.html")

    # if resp.status_code == 200:
    #     data = eval(resp.text)
    #     userinfo = {
    #         'nickname': data['nickname'],
    #         'openid': data['openid'],
    #         'unionid': data['unionid'],
    #         'portraits': data['portraits'],
    #         'sex': data['sex'],
    #         'address': data['address'],
    #         'language': data['language'],
    #         'subscribe_tiem': data['subscribe_tiem'],
    #         'province': data['province'],
    #         'headimgurl': data['headimgurl']
    #     }
    # else:
    #     return "登录失败"
    # # Love_user.add_user(**userinfo)
    # # return render_template('index.html')
    # return resp

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