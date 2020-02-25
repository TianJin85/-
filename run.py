# -*- encoding: utf-8 -*-
"""
@File    : run.py
@Time    :  2020/2/25 16:26
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin import db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.app import create_app

from app.models import love

app = create_app(environment='development')
manager = Manager(app)
# init  migrate upgrade
# 模型 -> 迁移文件 -> 表
# 1.要使用flask_migrate,必须绑定app和DB
migrate = Migrate(app, db)

# 2.把migrateCommand命令添加到manager中。
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
