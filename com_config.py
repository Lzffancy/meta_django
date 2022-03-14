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
            "class": "logging.handlers.TimedRotatingFileHandler",  # 输出日志文件
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
        "django": {
            "handlers": ["console", "mail_admins", "file"],  # 三选一handler，会根据handle的等级触发
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server", "file"],
            "level": "INFO",
            "propagate": False,  # 错误等级不传递
        },
    },
}
