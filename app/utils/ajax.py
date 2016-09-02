# coding:utf-8
from django.http import HttpResponse
from django.core.serializers.json import json, DjangoJSONEncoder


class Result:
    code = 201  # 200成功  其他失败
    msg = '操作失败'  # 提示语
    data = {}  # 操作返回数据

    def __init__(self, code=201, msg='', data={}):
        self.code = code
        self.msg = msg
        self.data = data

    def code(self, code=201):
        self.code = code

    def msg(self, msg=' 操作失败'):
        self.msg = msg

    def data(self, data={}):
        self.data = data


"""
字典转换为json
code 200成功
msg 返回提示语
"""


def ajax_json(request, result):
    zidian = {'data': result.data, 'code': result.code, 'msg': result.msg}

    ss = json.dumps(zidian, cls=DjangoJSONEncoder)

    return HttpResponse(ss)
