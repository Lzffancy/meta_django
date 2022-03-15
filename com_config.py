"""
通用的配置变量
"""

# logging
# 此段是django的默认日志系统 对其进行修改，控制台输出日志记录log文件下
# \meta_django_box\log
# todo 1.日志行需要带有请求的ip 2.日志格式 用户业务日志需要和系统日志分开，日志格式美化
DEFAULT_LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        # dj默认
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "{levelname}:{asctime} {message}",
            "datefmt": '%Y-%m-%d %H:%M:%S',
            "style": "{",
        },

        "standard": {},
        "simple": {},
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",  # 输出到控制台
        },
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",  # 输出日志文件
            "filename": "log/django_info.log",
            "formatter": "django.server",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",  # 输出到邮件系统系统
        },
    },
    "loggers": {
        "root": {  # 保底日志
            "handlers": ["file"],
            'level': 'INFO',
        },
        "django": {
            "handlers": ["console", "mail_admins"],  # 三选一handler，会根据handle的等级触发
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,  # 错误等级不传递
        },
    },
}

# LOGGING = {
#     'version': 1,
#     # 禁用日志
#     'disable_existing_loggers': False,
#     'loggers': {
#         '': {
#             # 将系统接受到的体制，交给handler去处理
#             'handlers': ['console'],
#             'level': 'INFO',
#         }
#     },
#     'handlers': {
#         'default': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': '%s/%s' % (LOG_PATH, 'asm.log'),
#             'maxBytes': 1024 * 1024 * 5,  # 文件大小
#             'backupCount': 5,  # 备份数
#             # 'formatter': 'standard',  # 输出格式
#             'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
#         },
#         'console': {
#             # handler将日志信息存放在day6/logs/sys.log
#             'filename': '%s/%s' % (LOG_PATH, 'asm.log'),
#             'level': 'INFO',
#             # 指定日志的格式
#             'formatter': '',
#             # 备份
#             'class': 'logging.handlers.RotatingFileHandler',
#             # 日志文件大小：5M
#             'maxBytes': 5 * 1024 * 1024,
#             'encoding':"utf-8"
#         }
#     },
#     'formatters': {
#         'default': {
#             'format': '%(asctime)s %(message)s'
#         }
#     }
# }
