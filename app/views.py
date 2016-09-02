# coding:utf-8

from django.http import HttpResponse
import simplejson as json
from app.utils.ajax import Result, ajax_json
from django.views.decorators.csrf import csrf_exempt
from app.models import User
from datetime import datetime
from django.shortcuts import render
from app.utils.convert_dict import convert_class_to_dict
from django.forms.models import model_to_dict


def index(request):
    return render(request, 'a.html')


@csrf_exempt
def login(request):
    post = json.loads(request.body)
    phone = post.get('phone', '')
    password = post.get('password', '')
    result = Result()

    try:
        users = User.objects.get(phone=phone)
        # user = users[0]
        if users.password == password:
            data = {'name': users.name, 'phone': users.phone, 'image': users.image,
                    'add_time': datetime.strftime(users.add_time, '%Y-%m-%d %H:%M:%S')}

            result.code = 200
            result.data = model_to_dict(users, exclude=["add_time", "last_time"])
            # result.data = model_to_dict(users, exclude=["add_time"])  # convert_class_to_dict(model_to_dict(users))
        else:
            result.code = 201
            result.msg = '密码不正确'
    except:
        result.code = 202
        result.msg = '用户不存在' + phone

    return HttpResponse(ajax_json(request, result))


@csrf_exempt
def register(request):
    '''
    用户注册
    '''

    post = json.loads(request.body)

    username = post.get('username', '')
    password = post.get('password', '')
    phone = post.get('phone', '')

    result = Result()
    if username == '':
        result.msg = '用户名不能为空'
    if password == '':
        result.msg = '密码不能为空'
    if phone == '':
        result.msg = '手机号不能为空'

    try:
        User.objects.get(phone=phone)
        result.msg = '用户已存在，请直接登录'
    except:
        usr = User.objects.create(name=username, password=password, phone=phone, add_time=datetime.now())
        result.code = 200
        result.msg = '注册成功'

        data = {'name': usr.name,
                'phone': usr.phone,
                'add_time': datetime.strftime(usr.add_time, '%Y-%m-%d %H:%M:%S')}

        result.data = data

    return HttpResponse(ajax_json(request, result))
