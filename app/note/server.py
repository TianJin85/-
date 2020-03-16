#!/usr/bin/env python
#coding=utf-8
from random import choice

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


class NoetServer:

    def __init__(self, phone):
        self.code_dict = self.random_code()
        self.phone = phone

    def send_code(self):
        client = AcsClient("LTAI4FcXR2ChjYjD57x9Cyn6", "hHL9Xn263xnNZ3uQFrV6Xsvi9Xe40x", 'cn-hangzhou')
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https') # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers', str(self.phone))
        request.add_query_param('SignName', "安顺之恋")
        request.add_query_param('TemplateCode', "SMS_185235175")
        # request.add_query_param('TemplateParam', "{\"code\":\"5200\"}")
        request.add_query_param('TemplateParam', self.code_dict)

        response = client.do_action_with_exception(request)
        # python2:  print(response)
        return str(response, encoding='utf-8')

    def random_code(self):
        """
        产生四位数的随机验证码
        :return:
        """

        TemplateParam = "123456789"
        code = []
        for i in range(4):
            code.append(choice(TemplateParam))

        code_dict = {"code": ''.join(code)}
        return code_dict


if __name__ == '__main__':
    noet = NoetServer("13618570390")


    print(noet.send_code(), noet.code_dict)