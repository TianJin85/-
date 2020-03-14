# -*- encoding: utf-8 -*-
"""
@File    : love_forms.py
@Time    :  2020/2/25 17:51
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin import manager
from wtforms import DateTimeField, PasswordField, FieldList, IntegerField, StringField, Form, FloatField
from wtforms.validators import DataRequired, Regexp, EqualTo, length, Optional, NumberRange

# from lin.forms import Form


class MessageForm(Form):
    username = StringField("用户姓名", validators=[DataRequired(message="用户名不能为空")])
    phone = StringField("电话号码", validators=[
        DataRequired("电话号码不能为空"),
        Regexp(r'[0-9]{11}', message="电话号码必须是11位0-9组成的数字")
    ])
    cardid = StringField("身份证号码", validators=[
        DataRequired("身份证不能为空"),
        Regexp(r'[0-9]{18}', message="身份证号码必须是18位0-9组成的数字")
    ])
    wechat = StringField("微信号", validators=[DataRequired(message="微信号不能为空")])
    qq = StringField("QQ号", validators=[DataRequired(message="QQ号不能为空")])
    school = StringField("毕业学校",validators=[DataRequired(message="毕业学校不能为空")])
    stature = StringField("身高", validators=[DataRequired(message="身高不能为空")])
    weight = StringField("体重", validators=[DataRequired(message="体重不能为空")])
    workunit = StringField("工作单位", validators=[DataRequired(message="工作单位不能为空")])
    occupation = StringField("职业", validators=[DataRequired(message="职业不能为空")])

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


class ctivity(Form):

    name = StringField("活动名称", validators=[DataRequired(message="活动名称不能为空")])
    adderss = StringField("活动地址", validators=[DataRequired(message="活动地址不能为空")])
    testarea = StringField("活动简介", validators=[DataRequired(message="活动简介不能为空")])
    date = DateTimeField("活动时间", validators=[DataRequired(message="活动时间不能为空")])
    rule = StringField("活动规则", validators=[DataRequired(message="活动规则不能为空")])
    initiator = StringField("发起人", validators=[DataRequired(message="发起人不能为空")])
    money = FloatField("活动金额",validators=[DataRequired(message="活动金额不能为空")])


