# -*- encoding: utf-8 -*-
"""
@File    : user_forms.py
@Time    :  2020/2/25 17:51
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin import manager
from wtforms import DateTimeField, PasswordField, FieldList, IntegerField, StringField
from wtforms.validators import DataRequired, Regexp, EqualTo, length, Optional, NumberRange
import time

from lin.forms import Form

class RegisterForm(Form):
    pass