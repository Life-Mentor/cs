from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):

    USER_GENDER_TYPE = ( ('male', '男'), ('female', '女'),)

    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="账号")
    name = models.CharField('昵称',max_length=32)
    user_info = models.CharField('个人简介', max_length=100, blank=True, default='')
    gexing = models.CharField('个性签名', max_length=100, blank=True, default='')
    gender = models.CharField('性别', max_length=6, choices=USER_GENDER_TYPE, default='male')
    icon = models.CharField('用户头像',max_length=255)

    class Meta:
        verbose_name = '用户数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.owner.username
