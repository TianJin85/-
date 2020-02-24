# -*- encoding: utf-8 -*-
"""
@File    : add_love_user.py
@Time    :  2020/2/21 15:55
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.core import User
from lin.db import db

from app.app import create_app
from app.models.love import Love_user


def main():
    app = create_app()
    with app.app_context():
        with db.auto_commit():
            # 创建一个超级管理员
            user = Love_user()
            user.Username = "夏枯草"
            user.Address = "贵阳"
            user.Sex = "男"
            user.Province = "贵阳"
            user.Openid
            db.session.add(user)


if __name__ == '__main__':
    try:
        main()
        print("新增超级管理员成功")
    except Exception as e:
        raise e
