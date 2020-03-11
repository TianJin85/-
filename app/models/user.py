# -*- encoding: utf-8 -*-
"""
@File    : user.py
@Time    :  2020/3/10 15:36
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from app.models.love import Love_user


class User(Love_user):
    """
    模型操作方法
    """
    @classmethod
    def add_user(cls, nickname, openid, unionid, portraits, sex, address, language, subscribe_tiem, province,
                 headimgurl):
        user = Love_user.query.filter_by(openid=openid).first()
        if user is None:
            Love_user.create(
                nickname=nickname,
                Openid=openid,
                Unionid=unionid,
                Portraits=portraits,
                Sex=sex,
                Address=address,
                Language=language,
                Subscribe_tiem=subscribe_tiem,
                Province=province,
                Headimgurl=headimgurl,
                vip=0,
                commit=True
            )

    @classmethod
    def get_id_vip(cls, openid):
        userid = None
        vip = None
        user = Love_user.query.filter_by(openid=openid).first()
        if user:
            userid = user.id
            vip = user.vip
        return {"userid": userid, "vip": vip}

    @classmethod
    def get_user_id(cls, openid):
        userid = None
        user = Love_user.query.filter_by(openid=openid).first()
        if user:
            userid = user.id

        return userid

    @classmethod
    def add_vip(cls, userid):
        user = Love_user.query.filter_by(id=userid).first()
        if user:
            if user.id != 1:
                user.update(
                    vip=1,
                    commit=True
                )

    @classmethod
    def remove_vip(cls, userid):
        user = Love_user.query.filter_by(id=userid).first()
        if user:
            if user.id != 1:
                user.update(
                    vip=0,
                    commit=True
                )

    @classmethod
    def delete_user(cls, id):
        user = Love_user.query.filter_by(id=id).first()
        if user is None:
            return
        user.hard_delete(commit=True)

    @classmethod
    def add_openid(cls, openid, headimgurl):
        user = Love_user.query.filter_by(openid=openid).first()
        if user is None:
            Love_user.create(
                openid=openid,
                headimgurl=headimgurl,
                vip=0,
                commit=True
            )

        return user
