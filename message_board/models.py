from django.db import models


# Create your models here.
class MessageBoard(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=32)
    content = models.TextField()
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "MessageBoard"
