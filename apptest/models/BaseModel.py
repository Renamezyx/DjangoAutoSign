from django.db import models


class BaseModel(models.Model):
    """
    model 基类
    """

    class Meta:
        abstract = True
        ordering = ['-created_time']

    created_time = models.DateTimeField(auto_now_add=True, help_text=u'创建时间')
    last_update_time = models.DateTimeField(auto_now=True, help_text=u'修改时间')

    def __str__(self):
        raise NotImplementedError
