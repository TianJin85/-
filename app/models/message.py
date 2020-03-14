# -*- encoding: utf-8 -*-
"""
@File    : message.py
@Time    :  2020/3/10 15:38
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from datetime import datetime

from lin import db


from app.models.love import Love_message, Love_selection, session


class Message(Love_message):
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine("mysql+cymysql://tianjin:TJ307440205@211.149.250.67:3306/marriage")
    Session = sessionmaker(bind=engine)

    session = Session()

    @classmethod
    def add_message(cls, uid, username, census, cardid, stature, weight, wechat, qq, school, education, workunit,
                    occupation, \
                    profession, monthly, member, housing, rest, vehicle, marriage, phone, images, sex, age):
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
                sex=sex,
                age=int(age),
                commit=True
            )
        return True

    @classmethod
    def get_message(cls, userid):
        """
        处理个人数据
        :param userid:
        :return:
        """
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
            messifno["images"] = eval(mess.images)[0]

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
    def get_unenroll(cls, uid):
        """
        根据id进行查询个人的数据
        :param uid:
        :return: datainfo
        """
        datainfo = db.session.query(Love_message, Love_selection).filter_by(uid=uid).join(Love_selection).first()

        return datainfo

    @classmethod
    def get_index(cls):
        """
        查询所有的数据
        :return:
        """
        datainfo = db.session.query(Love_message, Love_selection).join(Love_selection).all()
        return datainfo

    @classmethod
    def get_sex(cls, sex):
        """
        根据性别收搜
        :param sex:
        :return:
        """
        return db.session.query(Love_message, Love_selection).filter_by(sex=sex).join(Love_selection).all()


    @classmethod
    def set_cardid(cls, cardid):
        """
        身份证数据处理
        :param cardid:
        :return:
        """
        messinfo = {}
        year = cardid[6:10]
        month = cardid[10:12]
        day = cardid[12:14]
        local = datetime.now()  # 获取当前时间

        age = int((local - datetime(int(year), int(month), int(day))).days / 365)
        messinfo["age"] = age
        sex = None
        print(cardid)
        if int(cardid[14:18]) % 2 == 0:  # 偶数为女
            sex = "女"
        else:
            sex = "男"

        messinfo["sex"] = sex
        return messinfo

    @classmethod
    def update_age_sex(cls, uid, sex, age):
        mess = Love_message.query.filter_by(uid=uid).first()
        if mess:
            mess.update(
                sex=sex,
                age=age,
                commit=True
            )



