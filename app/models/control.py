# -*- encoding: utf-8 -*-
"""
@File    : control.py
@Time    :  2020/2/26 11:35
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin import db

from app.app import create_app
from app.models.love import Love_payment, Love_user, Love_ctivity, Love_message

app = create_app()


class love_user:

    user = Love_user()

    def __init__(self, Username, Openid, Unionid, Portraits, Sex, Address, Language, Subscribe_tiem, Province):
        self.Username = Username
        self.Openid = Openid
        self.Unionid = Unionid
        self.Portraits = Portraits
        self.Sex = Sex
        self.Address = Address
        self.Language = Language
        self.Subscribe_tiem = Subscribe_tiem
        self.Province = Province

    def add_user(self):
        while app.app_context():
            while db.auto_commit():
                self.user.Username = self.Username
                self.user.Openid = self.Openid
                self.user.Unionid = self.Unionid
                self.user.Portraits = self.Portraits
                self.user.Sex = self.Sex
                self.user.Address = self.Address
                self.user.Language = self.Language
                self.user.Subscribe_tiem = self.Subscribe_tiem
                self.user.Portraits = self.Province

                db.session.add(self.user)



