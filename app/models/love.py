# -*- encoding: utf-8 -*-
"""
@File    : love.py
@Time    :  2020/2/20 10:46
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.interface import InfoCrud as Base

from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, Boolean


class Love_user(Base):

    __tablename__ = "love_user"
    Id = Column(Integer, primary_key=True, autoincrement=True, comment="用户id")
    Username = Column(String(32), comment="用户名称")
    Openid = Column(String(62), comment="用户标识")
    Unionid = Column(String(62), comment="接口凭证")
    Portraits = Column(String(62), comment="用户头像")
    Sex = Column(String(120), comment="用户性别")
    Address = Column(String(4), comment="所在城市")
    Language = Column(String(15), comment="语言")
    Subscribe_tiem = Column(String(20), comment="关注时间")
    Province = Column(String(20), comment="所在的省份")


class Love_message(Base):
    __tablename__ = "love_message"
    Id = Column(Integer, primary_key=True, autoincrement=True, comment="信息id")
    Uid = Column(Integer, ForeignKey("love_user.Id"), comment="用户id")
    Phone = Column(Integer, nullable=False, comment="电话号码")
    Cardid = Column(String(28), nullable=False, comment="身份证号码")
    Census = Column(String(62), nullable=False, comment="户籍所在地")
    Images = Column(String(62), nullable=False, comment="用户图片")
    Hobby = Column(String(120), nullable=False, comment="兴趣爱好")
    Stature = Column(String(4), nullable=False, comment="身高")
    Weight = Column(String(4), nullable=False, comment="体重")
    Blood = Column(String(6), nullable=False, comment="血型")
    Nation = Column(String(12), nullable=False, comment="民族")
    Standards = Column(String(200), nullable=False, comment="择偶标准")
    Education = Column(String(20), nullable=False, comment="学历")
    Vehicle = Column(String(3), nullable=False, comment="是否有车")
    Monthly = Column(Float, nullable=False, comment="月薪")
    Profession = Column(String(12), nullable=False, comment="职业性质")
    Marriage = Column(String(20), nullable=False, comment="婚恋情况")
    Housing = Column(String(62), nullable=False, comment="住房情况")
    Personage = Column(String(500), nullable=False, comment="个人介绍")
    Logindate = Column(Integer, nullable=False, comment="登录次数")


class Love_payment(Base):

    __tablename__ = 'love_payment'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Uid = Column(Integer, ForeignKey("love_user.Id"), comment="用户id")
    Status = Column(Boolean, nullable=False, comment="支付状态")
    Money = Column(Float(9), nullable=False, comment="支付金额")
    Accounts = Column(String(32), nullable=False, comment="转账单号")


class Love_ctivity(Base):

    __tabelname__ = 'love_ctivity'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(62), nullable=False, comment="活动名称")
    Adderss = Column(String(32), nullable=False, comment="活动地址")
    Testarea = Column(String(5000), nullable=False, comment="活动简介")
    Date = Column(DateTime, nullable=False, comment="活动时间")
    Num = Column(Integer, nullable=True, comment="报名次数")


