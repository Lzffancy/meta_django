import time
import json
import traceback

from django.utils.deprecation import MiddlewareMixin
import urllib.parse
# 获取日志logger
import logging

logger = logging.getLogger(__name__)


class LogMiddle(MiddlewareMixin):
    # 日志处理中间件
    def process_request(self, request):
        # 存放请求过来时的时间
        request.init_time = time.time()
        return None

    def process_response(self, request, response):
        try:
            # 耗时
            localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # 请求路径
            path = request.path
            # 请求方式
            method = request.method
            # 响应状态码
            status_code = response.status_code
            # 响应内容
            content = response.content
            # 记录信息
            content = str(content.decode('utf-8'))
            content = urllib.parse.unquote(content)
            message = '%s %s %s %s' % (path, method, status_code, content)
            # print(message)
            logger.info(message)
        except Exception as e:
            logger.critical(f"log something wrong:{traceback.format_exc()}")
        return response
