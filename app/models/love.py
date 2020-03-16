# -*- encoding: utf-8 -*-
"""
@File    : love.py
@Time    :  2020/2/20 10:46
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from datetime import datetime

from lin import db
from lin.interface import InfoCrud as Base

from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, Boolean, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()

Session.configure(bind=engine)

session = Session()


class Love_user(Base):

    __tablename__ = "love_user"
    id = Column("id", Integer, primary_key=True, autoincrement=True, comment="用户id")
    ctivity_id = Column("ctivity_id", String(120), comment="参与活动id")
    nickname = Column("nickname", String(32), comment="用户名称")
    openid = Column("openid", String(62), comment="用户标识", unique=True)
    unionid = Column("unionid", String(62), comment="接口凭证")
    portraits = Column("portraits", String(200), comment="用户头像")
    sex = Column("sex", String(120), comment="用户性别")
    address = Column("address", String(4), comment="所在城市")
    language = Column("language", String(15), comment="语言")
    subscribe_tiem = Column("subscribe", DateTime, default=datetime.now, comment="关注时间")
    province = Column("province", String(20), comment="所在的省份")
    collect = Column('collect', String(120), comment="收藏")
    headimgurl = Column('headimgurl', String(200), comment="头像连接")
    vip = Column('vip', String(2), comment="是否是VIP")


class Love_search_message(Base):
    id = Column("id", Integer, primary_key=True, autoincrement=True, comment="查看id")
    uid = Column("uid", Integer, ForeignKey("love_user.id"), comment="用户id", unique=True)
    search_wx = Column("search_wx", String(500), comment="查看过我微信的人")
    search_qq = Column("search_qq", String(500), comment="查看过我QQ的人")
    search_phone = Column("search_phone", String(500), comment="查看过我电话号码的人")


class Love_message(Base):
    __tablename__ = "love_message"
    id = Column("id", Integer, primary_key=True, autoincrement=True, comment="信息id")
    username = Column("username", String(15), nullable=False, comment="用户姓名")
    uid = Column("uid", Integer, ForeignKey("love_user.id"), comment="用户id", unique=True)
    census = Column("census", String(62),  comment="户籍所在地")
    cardid = Column("cardid", String(28), nullable=False, comment="身份证号码")
    sex = Column("sex", String(3), comment="性别")
    age = Column("age", Integer, comment="年龄")
    stature = Column("stature", String(4), comment="身高")
    weight = Column("weight", String(4),  comment="体重")
    phone = Column("phone", String(13), nullable=False, comment="电话号码")
    wechat = Column("wechat", String(16), nullable=False, comment="微信号")
    qq = Column("qq", String(16), nullable=False, comment="QQ号")
    school = Column("school", String(32),  comment="毕业学校")
    images = Column("images", String(200), comment="用户图片")
    education = Column("education", String(20), comment="学历")
    vehicle = Column("vehicle", String(3), comment="是否有车")
    monthly = Column("monthly", String(30), comment="月薪范围")
    workunit = Column("workunit", String(32), comment="工作单位")
    occupation = Column("occupation", String(32), comment="职业")
    profession = Column("profession", String(12), comment="职业性质")
    member = Column("member", String(32), comment="家庭成员")
    marriage = Column("marriage", String(20), comment="婚恋情况")
    housing = Column("housing", String(62), comment="住房情况")
    rest = Column("rest", String(500), comment="其他要求")


class Love_selection(Base):

    __tablename__ = 'love_selection'
    id = Column("id", Integer, primary_key=True, autoincrement=True, comment="择偶id")
    mid = Column("mid", Integer, ForeignKey("love_message.id"), comment="用户信息id", unique=True)
    marriage = Column("marriage", String(12),comment="婚史情况")
    age = Column("age", String(30), comment="年龄")
    stature = Column("stature", String(4), comment="最低身高要求")
    weight = Column("weight", String(10), comment="体重范围")
    monthly = Column("monthly", String(30), comment="月薪范围")
    housing = Column("housing", String(62), comment="住房情况")
    vehicle = Column("vehicle", String(3), comment="是否有车")
    children = Column("children", String(10), comment="有无子女")
    census = Column("census", String(62), comment="户籍所在地")
    rests = Column("rests", String(500), comment="其他")


class Love_payment(Base):

    __tablename__ = 'love_payment'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    uid = Column("uid", Integer, ForeignKey("love_user.id"), comment="用户id")
    status = Column("status", Boolean, nullable=False, comment="支付状态")
    money = Column("money", Float, nullable=False, comment="支付金额")
    accounts = Column("accounts", String(32), nullable=False, comment="转账单号")


class Love_record(Base):
    __tablename__ = 'love_record'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    pid = Column("pid", Integer, ForeignKey("love_payment.id"), comment="支付金额")
    money = Column("money", Float, comment="消費金額")
    balance = Column("balance", Float, comment="余额")
    money_Sum = Column("money_sum", Float, comment="充值金额")


class Love_ctivity(Base):

    __tabelname__ = 'love_ctivity'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(62), nullable=False, comment="活动名称")
    address = Column("address", String(32), nullable=False, comment="活动地址")
    testarea = Column("testarea", String(20000), nullable=False, comment="活动简介")
    date = Column("date", DateTime, nullable=False, comment="活动时间")
    rule = Column("rule", String(500), comment="活动规则")
    message = Column("message", String(200), comment="其他信息")
    initiator = Column("initiator", String(10), comment="发起人")
    money = Column("money", Float, comment="活动收费金额")
    images = Column("images", String(60), comment="活动封面图片")
    num = Column("num", Integer, comment="报名次数")


