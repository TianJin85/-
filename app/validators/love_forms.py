# -*- encoding: utf-8 -*-
"""
@File    : love_forms.py
@Time    :  2020/2/25 17:51
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin import manager
from wtforms import DateTimeField, PasswordField, FieldList, IntegerField, StringField, FloatField
from wtforms.validators import DataRequired, Regexp, EqualTo, length, Optional, NumberRange
import time

from lin.forms import Form


class MessageForm(Form):
    UserName = StringField("用户姓名", DataRequired())
    Uid = IntegerField("用户姓名", DataRequired())
    Phone = IntegerField("用户id", DataRequired())
    Cardid = StringField("电话号码", validators=[
        DataRequired("电话号码不能为空"),
        Regexp(r'[0-9]{11}', manager="电话号码必须是11位0-9组成的数字")
    ])
    Census = StringField("身份证号码", validators=[
        DataRequired("身份证不能为空"),
        Regexp(r'[0-9]{28}', manager="身份证号码必须是28位0-9组成的数字")
    ])
    Wechat = StringField("户籍所在地不能为空", DataRequired())
    Qq = StringField("微信号不能空", DataRequired())
    School = StringField("QQ号不能为空", DataRequired())
    # Images = StringField("毕业学校", DataRequired())
    # Hobby = StringField("用户图片", DataRequired())
    # Stature = StringField("兴趣爱好", DataRequired())
    # Weight = StringField("身高不能为空", DataRequired())
    # Blood = StringField("体重", DataRequired())
    # Nation = StringField("血型", DataRequired())
    # Education = StringField("民族", DataRequired())
    # Vehicle = StringField("学历", DataRequired())
    # Monthly = StringField("是否有车", DataRequired())
    # Workunit = StringField("月薪", DataRequired())
    # Occupation = StringField("工作单位", DataRequired())
    # Profession = StringField("职业", DataRequired())
    # Member = FloatField("职业性质", DataRequired())
    # Marriage = StringField("家庭成员", DataRequired())
    # Housing = StringField("婚恋情况", DataRequired())
    # Children = StringField("住房情况", DataRequired())
    # Personage = StringField("有无子女", DataRequired)


# class StandatdsForm(Form):
#     Marriage = StringField("婚史情况", validators=[])
#     Sex = IntegerField("年龄", validators=[])
#     Stature = StringField("最低身高要求", validators=[])
#     Weight = StringField("体重", validators=[])
#     Monthly = StringField("月薪", validators=[])
#     Housing = StringField("住房情况", validators=[])
#     Vehicle = StringField("是否有车", validators=[])
#     Children = StringField("有无子女", validators=[])
#     Census = StringField("户籍所在地", validators=[])
#     Rests = StringField("其他", validators=[])

