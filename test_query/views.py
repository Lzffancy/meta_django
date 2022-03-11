import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from test_query.models import Message_board
from django.db import connection


def index(request):
    # 使用原生游标连接避开orm,需要注意sql注入风险
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM meta_django_box.test_query_message_board;")
        # orm层的执行原生sql
        # for m in Message_board.objects.raw('SELECT * FROM meta_django_box.test_query_message_board;'):
        #     print(m._dict_)
        rows = cursor.fetchall()
        res = {}
        for i in range(0, len(rows)):
            res[i] = rows[i][0:3]
    return HttpResponse(str(res))
