# -*- encoding: utf-8 -*-
"""
@File    : message.py
@Time    :  2020/3/10 15:38
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from datetime import datetime

from app.models.love import Love_message


class Message(Love_message):

    @classmethod
    def add_message(cls, uid, username, census, cardid, stature, weight, wechat, qq, school, education, workunit,
                    occupation, \
                    profession, monthly, member, housing, rest, vehicle, marriage, phone, images):
        mess = Love_message.query.filter_by(uid=uid).first()
        if mess is None:
            Love_message.create(
                uid=uid,
                username=username,
                census=census,
                cardid=cardid,
                stature=stature,
                weight=weight,
                wechat=wechat,
                qq=int(qq),
                school=school,
                education=education,
                workunit=workunit,
                occupation=occupation,
                profession=profession,
                monthly=monthly,
                member=member,
                housing=housing,
                rest=rest,
                vehicle=vehicle,
                marriage=marriage,
                phone=int(phone),
                images=str(images),
                commit=True
            )
        return True

    @classmethod
    def get_message(cls, userid):
        mess = Love_message.query.filter_by(uid=userid).first()
        messifno = {"username": "***", "stature": "***", "weight": "***", "education": "***", "images": "***",
                    "age": "***"}
        if mess is None:

            return messifno
        else:
            # 522228199610032811
            messifno["username"] = mess.username
            messifno["stature"] = mess.stature
            messifno["weight"] = mess.weight
            messifno["education"] = mess.education
            messifno["occupation"] = mess.occupation
            messifno["images"] = mess.images
            cardid = mess.cardid
            year = cardid[6:10]
            month = cardid[10:12]
            day = cardid[12:14]
            local = datetime.now()  # 获取当前时间

            age = int((local - datetime(int(1996), int(10), int(3))).days / 365)
            messifno["age"] = age
            sex = None
            if int(cardid[14:18]) % 2 == 0:  # 偶数为女
                sex = "女"
            else:
                sex = "男"

            messifno["sex"] = sex

            return messifno

    @classmethod
    def get_messid(cls, uid):
        mess_id = None
        mess = Love_message.query.filter_by(uid=uid).first()
        if mess is None:
            pass
        else:
            mess_id = mess.id

        return mess_id
    @classmethod
    def update_mess(cls, uid):
        mess = Love_message.query.filter_by(uid=uid).first()
        if mess is None:
            pass
        else:
            mess.update(
                cardid=522228199610032811,
                commit=True
            )
