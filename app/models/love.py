# -*- encoding: utf-8 -*-
"""
@File    : love.py
@Time    :  2020/2/20 10:46
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from datetime import datetime

from lin.interface import InfoCrud as Base

from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, Boolean


class Love_user(Base):

    __tablename__ = "love_user"
    Id = Column("id", Integer, primary_key=True, autoincrement=True, comment="用户id")
    nickname = Column("nickname", String(32), comment="用户名称")
    Openid = Column("openid", String(62), comment="用户标识", unique=True)
    Unionid = Column("unionid", String(62), comment="接口凭证")
    Portraits = Column("portraits", String(62), comment="用户头像")
    Sex = Column("sex", String(120), comment="用户性别")
    Address = Column("address", String(4), comment="所在城市")
    Language = Column("language", String(15), comment="语言")
    Subscribe_tiem = Column("subscribe", DateTime, default=datetime.now, comment="关注时间")
    Province = Column("province", String(20), comment="所在的省份")


class Love_message(Base):
    __tablename__ = "love_message"
    Id = Column("id", Integer, primary_key=True, autoincrement=True, comment="信息id")
    UserName = Column("username", String(15), nullable=False, comment="用户姓名")
    Uid = Column("uid", Integer, ForeignKey("love_user.id"), comment="用户id")
    Census = Column("census", String(62),  comment="户籍所在地")
    Cardid = Column("cardid", String(28), nullable=False, comment="身份证号码")
    Stature = Column("stature", String(4), comment="身高")
    Weight = Column("weight", String(4),  comment="体重")
    Phone = Column("phone", Integer, nullable=False, comment="电话号码")
    Wechat = Column("wechat", String(30), nullable=False, Column="微信号")
    Qq = Column("qq", Integer, nullable=False, comment="QQ号")
    School = Column("school", String(32),  comment="毕业学校")
    Images = Column("images", String(62), comment="用户图片")
    Hobby = Column("hobby", String(120), comment="兴趣爱好")
    Blood = Column("blood", String(6), comment="血型")
    Nation = Column("nation", String(12), comment="民族")
    Education = Column("education", String(20), comment="学历")
    Vehicle = Column("vehicle", String(3), comment="是否有车")
    Monthly = Column("monthly", Float, comment="月薪")
    Workunit = Column("workunit", String(32), comment="工作单位")
    Occupation = Column("occupation", String(32), omment="职业")
    Profession = Column("profession", String(12),comment="职业性质")
    Member = Column("member", String(32), comment="家庭成员")
    Marriage = Column("marriage", String(20), comment="婚恋情况")
    Housing = Column("housing", String(62), comment="住房情况")
    Children = Column("children", String(10), comment="有无子女")
    Personage = Column("presonage", String(500), comment="个人介绍")


class Love_standatds(Base):

    __tablename__ = 'love_standatds'
    Id = Column("id", Integer, primary_key=True, autoincrement=True, comment="择偶id")
    Marriage = Column("marriage", String(12), nullable=False, comment="婚史情况")
    Sex = Column("sex", Integer, nullable=Float, comment="年龄")
    Stature = Column("stature", String(4), nullable=False, comment="最低身高要求")
    Weight = Column("weight", String(4), nullable=False, comment="体重")
    Monthly = Column("monthly", Float, nullable=False, comment="月薪")
    Housing = Column("housing", String(62), nullable=False, comment="住房情况")
    Vehicle = Column("vehicle", String(3), nullable=False, comment="是否有车")
    Children = Column("children", String(10), nullable=False, comment="有无子女")
    Census = Column("census", String(62), nullable=False, comment="户籍所在地")
    Rests = Column("rests", String(500), comment="其他")



class Love_payment(Base):

    __tablename__ = 'love_payment'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Uid = Column(Integer, ForeignKey("love_user.id"), comment="用户id")
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


