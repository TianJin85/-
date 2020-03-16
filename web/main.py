# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    :  2020/3/11 16:38
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle

urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
