# -*- encoding: utf-8 -*-
"""
@File    : resdb.py
@Time    :  2020/2/25 11:04
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from redis import Redis, exceptions


class RedisDB:

    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db

    def __enter__(self):
        try:
            self.conn = Redis(host=self.host, port=self.port, db=self.db)
        except exceptions.TimeoutError as e:
            print(e)
        except exceptions.AuthenticationWrongNumberOfArgsError as e:
            print(e)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

