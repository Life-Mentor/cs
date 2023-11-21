from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    """ 废弃了，作者太菜了不会用User默认的东西 """

    USER_GENDER_TYPE = ( ('male', '男'), ('female', '女'),)

    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="账号")
    name = models.CharField('昵称',max_length=32)
    user_info = models.CharField('个人简介', max_length=100, blank=True, default='')
    gexing = models.CharField('个性签名', max_length=100, blank=True, default='')
    gender = models.CharField('性别', max_length=6, choices=USER_GENDER_TYPE, default='baomi')
    icon = models.CharField('用户头像',max_length=255)

    class Meta:
        verbose_name = '用户数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.owner.username

class User_Info(models.Model):

    name = models.CharField(max_length=32,verbose_name='账号')
    password = models.CharField(max_length=256)
    email = models.CharField('邮箱',max_length=52)
    user_info = models.CharField('个性签名',max_length=522,blank=True,null=True,default='')
    gexing = models.CharField('个性签名', max_length=100, blank=True, default='')
    xieyi = models.CharField('协议',max_length=5)
    icon = models.CharField('用户头像',max_length=255)

    class Meta:
        verbose_name = '用户数据'
        verbose_name_plural = verbose_name

class EmailVerifyRecord(models.Model):
    SEND_TYPE = (('register','注册'),('forget','找回密码'))
    code = models.CharField("验证码",max_length=20)
    email = models.EmailField('邮箱',max_length=32)
    send_type = models.CharField(choices=SEND_TYPE, default='register', max_length=32)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
