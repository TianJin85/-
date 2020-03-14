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
        """
        添加用户
        :param nickname:
        :param openid:
        :param unionid:
        :param portraits:
        :param sex:
        :param address:
        :param language:
        :param subscribe_tiem:
        :param province:
        :param headimgurl:
        :return:
        """
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
        """
        获取vip用户
        :param openid:
        :return:
        """
        userid = None
        vip = None
        user = Love_user.query.filter_by(openid=openid).first()
        if user:
            userid = user.id
            vip = user.vip
        return {"userid": userid, "vip": vip}

    @classmethod
    def get_user_id(cls, openid):
        """
        根据openid获取用户信息
        :param openid:
        :return:
        """
        userid = None
        user = Love_user.query.filter_by(openid=openid).first()
        if user:
            userid = user.id

        return userid

    @classmethod
    def add_vip(cls, userid):
        """
        添加vip
        :param userid:
        :return:
        """
        user = Love_user.query.filter_by(id=userid).first()
        if user:
            if user.id != 1:
                user.update(
                    vip=1,
                    commit=True
                )

    @classmethod
    def remove_vip(cls, userid):
        """
        移除vip
        :param userid:
        :return:
        """
        user = Love_user.query.filter_by(id=userid).first()
        if user:
            if user.id != 1:
                user.update(
                    vip=0,
                    commit=True
                )

    @classmethod
    def delete_user(cls, id):
        """
        删除用户
        :param id:
        :return:
        """
        user = Love_user.query.filter_by(id=id).first()
        if user is None:
            return
        user.hard_delete(commit=True)

    @classmethod
    def add_openid(cls, openid, headimgurl):
        """
        微信公众授权登录
        :param openid:
        :param headimgurl:
        :return:
        """
        user = Love_user.query.filter_by(openid=openid).first()
        if user is None:
            Love_user.create(
                openid=openid,
                headimgurl=headimgurl,
                vip=0,
                commit=True
            )

        return True

    def collect(self, id, cid):
        """
        用户收藏
        :param id:
        :param cid:
        :return:
        """
        collect_cid = []
        user = Love_user.query.filter_by(id=id).first()
        collect_cid.append(cid)
        if user:
            if user.collect is None:
                user.update(
                    collect=str(collect_cid),
                    commit=True
                )

            else:
                if cid in user.collect:
                    pass
                else:
                    collect_list = eval(user.collect)
                    collect_list.append(cid)
                    user.update(
                        collect=str(collect_list),
                        commit=True
                    )
        return True

    @classmethod
    def my_collect(cls, id):
        user = Love_user.query.filter_by(openid=id).first()

        if user:
            return user.collect
        else:
            return None



