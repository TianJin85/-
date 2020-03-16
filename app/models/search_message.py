# -*- encoding: utf-8 -*-
"""
@File    : search_message.py
@Time    :  2020/3/14 11:39
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from datetime import datetime

from app.models.love import Love_search_message


class Serch_message(Love_search_message):

    @classmethod
    def search_wx(cls, id, uid):
        """
        查看微信號碼的人
        :param id: 用戶id
        :param uid:被查看的用户id
        :return:
        """
        mess = Love_search_message.query.filter_by(uid=uid).first()

        wx_list = [{"date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "id": id}]
        if mess is None:
            Love_search_message.create(
                uid=uid,
                search_wx=str(wx_list),
                commit=True
            )
        else:
            if mess.search_wx is None:
                mess.update(
                    search_wx=str(wx_list),
                    commit=True
                )
            else:
                if id in mess.search_wx:
                    pass
                else:
                    searchar = eval(mess.search_wx)
                    searchar.append({"date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "id": id})
                    mess.update(
                        search_wx=str(searchar),
                        commit=True
                    )
        return True

    @classmethod
    def search_qq(cls, id, uid):
        """
        查看QQ的人
        :param id: 用户id
        :param uid: 被查看的用户
        :return:
        """
        mess = Love_search_message.query.filter_by(uid=uid).first()

        qq_list = [{"date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "id": id}]
        if mess is None:
            Love_search_message.create(
                uid=uid,
                search_qq=str(qq_list),
                commit=True
            )
        else:
            if mess.search_qq is None:
                mess.update(
                    search_qq=str(qq_list),
                    commit=True
                )
            else:
                if id in mess.search_qq:
                    pass
                else:
                    searchar = eval(mess.search_qq)
                    searchar.append({"date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "id": id})
                    mess.update(
                        search_qq=str(searchar),
                        commit=True
                    )
        return True

    @classmethod
    def search_phone(cls, id, uid):
        """
        查看电话号码的人
        :param id: 用户id
        :param uid: 被查看的用户id
        :return:
        """
        mess = Love_search_message.query.filter_by(uid=uid).first()

        phone_list = [{"date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "id": id}]
        if mess is None:
            Love_search_message.create(
                uid=uid,
                search_phone=str(phone_list),
                commit=True
            )
        else:
            if mess.search_phone is None:
                mess.update(
                    search_phone=str(phone_list),
                    commit=True
                )
            else:
                if id in mess.search_phone:
                    pass
                else:
                    searchar = eval(mess.search_phone)
                    searchar.append({"date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "id": id})
                    mess.update(
                        search_qq=str(searchar),
                        commit=True
                    )
        return True

    @classmethod
    def qq_list(cls, id):
        mess = Love_search_message.query.filter_by(uid=id).first()
        if mess:
            return mess.search_qq
        else:
            return None

    @classmethod
    def wx_list(cls, id):
        mess = Love_search_message.query.filter_by(uid=id).first()
        if mess:
            return mess.search_wx
        else:
            return True

    @classmethod
    def phone_list(cls, id):
        mess = Love_search_message.query.filter_by(uid=id).first()
        if mess:
            return mess.search_phone
        else:
            return None


