# -*- encoding: utf-8 -*-
"""
@File    : ctivity.py
@Time    :  2020/3/14 16:16
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from app.models.love import Love_ctivity


class Ctivity(Love_ctivity):

    @classmethod
    def add_ctivity(cls, name, adderss, testarea, date, rule, message, initiator, money, images):
        Love_ctivity.create(
            name=name,
            adderss=adderss,
            testarea=testarea,
            date=date,
            rule=rule,
            message=message,
            initiator=initiator,
            money=money,
            images=images,
            commit=True
        )
        return True

