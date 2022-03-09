from django.db import models


# Create your models here. db_table重写表名
class Message_board(models.Model):
    uid = models.CharField(max_length=16, primary_key=True)
    nick_name = models.CharField(max_length=16)
    message = models.TextField(max_length=258)
    created_date = models.DateTimeField(auto_now_add=True)
