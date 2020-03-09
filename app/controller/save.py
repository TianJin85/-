# -*- encoding: utf-8 -*-
"""
@File    : save.py
@Time    :  2020/3/9 9:18
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import base64
import os

from flask import url_for


class Save:

    def __init__(self, result):
        self.result = result
        self.imgpath = []

    def get_data(self):
        if "images_id1" in self.result and "images_src1" in self.result:
            images_id1 = self.result["images_id1"]
            images_src1 = self.result["images_src1"]
            self.savefile(id=images_id1, data=images_src1)   # 保存第一张图片图片

        if "images_id2" in self.result and "images_src2" in self.result:
            images_id2 = self.result["images_id2"]
            images_src2 = self.result["images_src2"]
            self.savefile(id=images_id2, data=images_src2)  # 保存第一张图片图片
        if "images_id3" in self.result and "images_src3" in self.result:
            images_id3 = self.result["images_id3"]
            images_src3 = self.result["images_src3"]
            self.savefile(id=images_id3, data=images_src3)  # 保存第一张图片图片

        return self.imgpath

    def savefile(self, id, data):

        try:
            images_base64 = data.split(",")[1]
            images_type = None
            if "png" in data:
                images_type = "png"
            elif "jpg" in data:
                images_type = "jpg"
            data = base64.b64decode(images_base64)
            with open(os.path.join(os.getcwd(), "app", "static", "userimg", \
                                   "{0}.{1}".format(id, images_type)), "wb") as f:
                f.write(data)
            self.imgpath.append(url_for("static", filename="userimg/{id}.{type}".format(id=id, type=images_type)))
        except:
            return False